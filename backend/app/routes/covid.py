import requests
from bs4 import BeautifulSoup
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from backend.app.crud.covid import (
    add_covid,
    get_covid,
    get_covid_by_report_no,
    get_all_covids,
    update_covid,
    delete_covid
)

from backend.app.models.covid import (
    ErrorResponseModel,
    ResponseModel,
    CovidSchema,
    UpdateCovidModel
)

from backend.send_email import send_email

CovidRouter = APIRouter()

@CovidRouter.post("/", response_description="Add covid data to database")
async def controller_add_covid(covid: CovidSchema = Body(...)):
    covid = jsonable_encoder(covid)
    new_covid = await add_covid(covid)
    return ResponseModel(new_covid, "Covid added successfully")

@CovidRouter.get("/", response_description="Get all covids from database")
async def controller_get_all_covids():
    covids = await get_all_covids()
    return ResponseModel(covids, "Retrived Covid data")


@CovidRouter.get("/list", response_description="Get all covid reports from dgs")
async def list_covid_from_dgs():
    covid_list_request_url = "https://covid19.min-saude.pt/relatorio-de-situacao/"
    get_covid_list_response = requests.get(covid_list_request_url)

    if get_covid_list_response.status_code != 200:
        return ErrorResponseModel("/list error" , covid_list_request_url.status_code, "Error getting list from DGS")
    
    soup = BeautifulSoup(get_covid_list_response.content, "html.parser")

    content_easy = soup.find(id="content_easy")
    report_list = content_easy.find_all("li")

    i = 0

    for report in report_list:
        if report.text.startswith("R"):
            begin_separator = "Relatório de Situação nº "
            middle_separator = " | "
            report_no = report.text.split(begin_separator)[1].split(middle_separator)[0]

            existing_covid = await get_covid_by_report_no(report_no=report_no)

            if existing_covid == None:
                download_url = report.find("a")["href"]
                covid = {
                    "report_no": report_no,
                    "download_url": download_url
                }
                covid = jsonable_encoder(covid)
                new_covid = await add_covid(covid)
                i += 1

                # send_email(covid)

    if i > 0:
        response_message = "Added new reports"
    else:
        response_message = "No new reports to add"

    return ResponseModel(
        data={
            "Count": i
        },
        message=response_message
        )
