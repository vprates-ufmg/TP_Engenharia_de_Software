from beanie import Document, Indexed


class Disciplina(Document):
    """
    Representa uma disciplina da Universidade.
    """

    id_disciplina: Indexed(str, unique=True)
    cod_disciplina: Indexed(str)
    nome: str
