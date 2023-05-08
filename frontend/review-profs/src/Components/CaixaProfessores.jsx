async function fetchProfessores(id_disciplina = "") {
  const headers = new Headers();
  headers.append("Content-Type", "application/json");
  const response = await fetch("http://127.0.0.1:5000/fetch_professores", {
    method: "POST",
    headers: headers,
    body: JSON.stringify({ disciplina_id: id_disciplina }),
  });

  const data = await response.json();
  const items = data.data;

  return (
    <select defaultValue="Selecione um(a) Professor(a)">
      {items.map((item) => (
        <option value={item.id}>{item.nome}</option>
      ))}
    </select>
  );
}
