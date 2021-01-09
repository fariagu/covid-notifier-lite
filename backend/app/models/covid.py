from typing import Optional, Any
from pydantic import BaseModel, Field
from http import HTTPStatus

class CovidSchema(BaseModel):
    report_no: int = Field(...)
    download_url: str = Field(...)
    date: str = Field(...)
    infected: int = Field(...)
    dead: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "report_no": "101",
                "download_url": "http://download/file.pdf",
                "date": "01/01/2021",
                "infected": "9000",
                "dead": "900"
            }
        }

class UpdateCovidModel(BaseModel):
    report_no: Optional[int]
    download_url: Optional[str]

    class Config():
        schema_extra = {
            "example": {
                "report_no": "101",
                "download_url": "http://download/file.pdf",
                "date": "01/01/2021",
                "infected": "9000",
                "dead": "900"
            }
        }

def ResponseModel(data: Any, message: str):
    return {
        "data": [data],
        "code": HTTPStatus.OK,
        "message": message
    }

def ErrorResponseModel(error: Any, code: HTTPStatus, message: str):
    return {
        "error": error,
        "code": code,
        "message": message
    }