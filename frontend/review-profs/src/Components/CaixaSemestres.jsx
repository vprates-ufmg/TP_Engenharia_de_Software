async function fetchSemestres(id_disciplina = "", id_professor = "") {
  const headers = new Headers();
  headers.append("Content-Type", "application/json");
  const response = await fetch("http://127.0.0.1:5000/fetch_semestres", {
    method: "POST",
    headers: headers,
    body: JSON.stringify({
      disciplina_id: id_disciplina,
      professor_id: id_professor,
    }),
  });

  const data = await response.json();
  const items = data.data;

  return (
    <select defaultValue="Selecione um Semestre">
      {items.map((item) => (
        <option value={item.nome}>{item.nome}</option>
      ))}
    </select>
  );
}
