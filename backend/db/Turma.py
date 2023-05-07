from beanie import Document, Indexed


class Turma(Document):
    cod_disciplina: Indexed(str)
    semestre: Indexed(str)
    id_disciplina: str
    uid_professor_ministrante: str
