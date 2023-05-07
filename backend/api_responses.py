from dataclasses import dataclass
from typing import Union, List


@dataclass
class GenericResponse:
    success: bool
    message: str


@dataclass
class UserData:
    id: str
    username: str


@dataclass
class ReviewData:
    autor: str
    content: str
    time: str
    votes: int
    semester: str
    disciplina: str
    professor: str


@dataclass
class UserResponse:
    success: bool
    message: str
    data: Union[UserData, None]


@dataclass
class ReviewResponse:
    success: bool
    message: str
    data: List[ReviewData]
