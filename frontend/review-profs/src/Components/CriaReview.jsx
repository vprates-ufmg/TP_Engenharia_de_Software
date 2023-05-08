import Cookies from "js-cookie";

async function criaReview(
  semestre,
  id_professor,
  id_disciplina,
  anonimo,
  conteudo
) {
  var session = Cookies.get("session");
  if (session === undefined) {
    session = "";
  }

  const headers = new Headers();
  headers.append("Content-Type", "application/json");
  const response = await fetch("http://127.0.0.1:5000/create_review", {
    method: "POST",
    headers: headers,
    body: JSON.stringify({
      semester: semestre,
      teacher_id: id_professor,
      disciplina_id: id_disciplina,
      is_anonymous: anonimo,
      content: conteudo,
      session: session,
    }),
  });

  let data = await response.json();
  if (!data.success) {
    alert(data.message);
    return;
  }

  data = data.data[0];

  return (
    <ul>
      <li>Autor: {data.autor}</li>
      <li>Semestre: {data.semester}</li>
      <li>Professor(a): {data.professor}</li>
      <li>Disciplina: {data.disciplina}</li>
      <li>Hora de postagem: {data.time}</li>
      <li>Votos: {data.votes}</li>
      <li>Conteúdo: {data.content}</li>
      <li>ID: {data.review_id}</li>
    </ul>
  );
}
