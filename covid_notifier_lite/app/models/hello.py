from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field
from http import HTTPStatus

class HelloSchema(BaseModel):
    message: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "message": "example message",
                "email": "email@address.com"
            }
        }

class UpdateHelloModel(BaseModel):
    message: Optional[str]
    email: Optional[EmailStr]

    class Config():
        schema_extra = {
            "example": {
                "message": "example message",
                "email": "email@address.com"
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