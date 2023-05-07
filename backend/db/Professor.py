from beanie import Document, Indexed


class Professor(Document):
    """
    Representa um professor da Universidade.
    """

    uid_professor: Indexed(str, unique=True)
    nome: str
