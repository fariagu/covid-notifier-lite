from typing import Optional, Any
from pydantic import BaseModel, Field
from http import HTTPStatus

class CovidSchema(BaseModel):
    report_no: int = Field(...)
    download_url: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "report_no": "001",
                "download_url": "http://download/file.pdf"
            }
        }

class UpdateCovidModel(BaseModel):
    report_no: Optional[int]
    download_url: Optional[str]

    class Config():
        schema_extra = {
            "example": {
                "report_no": "001",
                "download_url": "http://download/file.pdf"
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