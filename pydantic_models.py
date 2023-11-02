from typing import Any

from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator
from enum import Enum
from datetime import datetime


class NotificationKey(str, Enum):
    registration = "registration"
    new_message = "new_message"
    new_post = "new_post"
    new_login = "new_login"


class NotificationRequest(BaseModel):
    user_id: str = Field(max_length=24)
    key: NotificationKey
    target_id: str | None = Field(max_length=24, default=None)
    data: dict | None = Field(default=None)


class SaveInfo(BaseModel):
    id: str
    data: dict | None
    is_new: bool
    key: str
    target_id: str | None
    user_id: str
    timestamp: int

    @model_validator(mode="before")
    @classmethod
    def valid_id(cls, data: dict) -> dict:
        print()
        if db_id := data.get("_id"):
            data["id"] = str(db_id)
        return data


class Request(BaseModel):
    user_id: str
    skip: int
    limit: int


class Data(BaseModel):
    elements: int
    new: int
    request: Request
    list: list[SaveInfo]


class ListResponse(BaseModel):
    success: bool
    data: Data
