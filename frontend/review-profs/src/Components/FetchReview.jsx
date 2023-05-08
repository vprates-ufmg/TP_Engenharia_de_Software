async function fetchReview(
  sorting = 1,
  semestre,
  id_professor,
  id_disciplina,
  range_start = 0,
  range_end = 15
) {
  const headers = new Headers();
  headers.append("Content-Type", "application/json");
  const response = await fetch("http://127.0.0.1:5000/fetch_review", {
    method: "POST",
    headers: headers,
    body: JSON.stringify({
      sorting: sorting,
      semester: semestre,
      teacher_id: id_professor,
      disciplina_id: id_disciplina,
      range_start: range_start,
      range_end: range_end,
    }),
  });

  let data = await response.json();
  if (!data.success) {
    alert(data.message);
    return;
  }

  items = data.data;

  return (
    <ul>
      {items.map((item) => (
        <li key={item.review_id}>
          <p>Autor: {item.autor}</p>
          <p>Semestre: {item.semester}</p>
          <p>Professor(a): {item.professor}</p>
          <p>Disciplina: {item.disciplina}</p>
          <p>Hora de postagem: {item.time}</p>
          <p>Votos: {item.votes}</p>
          <p>Conteúdo: {item.content}</p>
          <p>ID: {item.review_id}</p>
        </li>
      ))}
    </ul>
  );
}
