from dataclasses import dataclass
from typing import Union


@dataclass
class GenericResponse:
    success: bool
    message: str


@dataclass
class UserData:
    id: str
    username: str


@dataclass
class UserResponse:
    success: bool
    message: str
    data: Union[UserData, None]
