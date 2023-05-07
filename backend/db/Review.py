from datetime import datetime
from uuid import uuid4
from beanie import Document, Indexed
from enum import IntEnum


class SortingMethod(IntEnum):
    """
    Enum que representa o método de ordenação de uma Review.
    """

    NEWEST_FIRST = 0
    OLDEST_FIRST = 1
    MOST_UPVOTED = 2
    LEAST_UPVOTED = 3


class Review(Document):
    """
    A publicação com a opinião do usuário a ser mostrada no site.
    """

    id_review: Indexed(str, unique=True)
    author: str
    author_id: str
    is_anonymous: bool
    content: str
    n_votes: int
    semester: str
    teacher_id: str
    disciplina_id: str
    time: str

    @classmethod
    async def create_review(
        cls,
        author_name: str,
        author_id: str,
        is_anonymous: bool,
        teacher_id: str,
        disciplina_id: str,
        semester: str,
        content: str,
    ) -> "Review":
        new = cls(
            id_review=str(uuid4()),
            author=author_name,
            author_id=author_id,
            is_anonymous=is_anonymous,
            teacher_id=teacher_id,
            disciplina_id=disciplina_id,
            content=content,
            n_votes=1,
            semester=semester,
            time=datetime.utcnow().isoformat(),
        )
        await new.save()
        return new
