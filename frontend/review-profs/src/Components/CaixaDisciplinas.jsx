async function fetchDisciplinas() {
  const response = await fetch("http://127.0.0.1:5000/fetch_disciplinas", {
    method: "GET",
  });

  const data = await response.json();
  const items = data.data;

  return (
    <select defaultValue="Selecione uma Disciplina">
      {items.map((item) => (
        <option value={item.id}>{item.nome}</option>
      ))}
    </select>
  );
}
