from beanie import Document, Indexed


class Turma(Document):
    """
    Representa uma turma da Universidade.
    Essa turma foi da matéria "id_disciplina"
    ofertada pelo professor "uid_professor_ministrante"
    no semestre "semestre".
    """

    cod_disciplina: Indexed(str)
    semestre: Indexed(str)
    id_disciplina: str
    uid_professor_ministrante: str
