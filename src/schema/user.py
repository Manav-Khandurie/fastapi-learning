# Databricks notebook source
from typing import List, Optional

from pydantic import BaseModel


class UserAddRequest(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class UserFetchResponse(BaseModel):
    id: int
    name: str
    msg: Optional[str] = None


class UserQueryResponse(BaseModel):
    message: str


class UserFetchAllResponse(BaseModel):
    users: List[UserFetchResponse]

    class Config:
        extra = "forbid"
