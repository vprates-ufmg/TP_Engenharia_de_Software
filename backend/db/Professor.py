from beanie import Document, Indexed

class Professor(Document):
    uid_professor: Indexed(str, unique=True)
    nome: str