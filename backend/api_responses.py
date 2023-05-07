"""
Esse arquivo inclui várias respostas de API codificadas em dataclasses.
"""
from dataclasses import dataclass
from typing import Union, List


@dataclass
class GenericResponse:
    success: bool
    message: str
    session: Union[str, None] = None


@dataclass
class SimpleData:
    id: Union[str, None]
    nome: str


@dataclass
class UserData:
    id: str
    username: str
    upvoted_reviews: List[str]
    downvoted_reviews: List[str]


@dataclass
class ReviewData:
    review_id: str
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
    session: str


@dataclass
class ReviewResponse:
    success: bool
    message: str
    data: List[ReviewData]


@dataclass
class SimpleResponse:
    success: bool
    message: str
    data: List[SimpleData]
