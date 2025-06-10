# Databricks notebook source
from typing import List, Optional

from pydantic import BaseModel


class UserAddRequest(BaseModel):
    """
    Represents a request to add a new user.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        description (Optional[str]): An optional description of the user.
    """

    id: int
    name: str
    description: Optional[str] = None


class UserFetchResponse(BaseModel):
    """
    Represents the response for fetching a user.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        msg (Optional[str]): An optional message related to the user.
    """

    id: int
    name: str
    msg: Optional[str] = None


class UserQueryResponse(BaseModel):
    """
    Represents a generic response for user queries.

    Attributes:
        message (str): A message related to the user query.
    """

    message: str


class UserFetchAllResponse(BaseModel):
    """
    Represents the response for fetching all users.

    Attributes:
        users (List[UserFetchResponse]): A list of user fetch responses.
    """

    users: List[UserFetchResponse]

    class Config:
        """
        Configuration for the UserFetchAllResponse model.
        """

        extra = "forbid"
