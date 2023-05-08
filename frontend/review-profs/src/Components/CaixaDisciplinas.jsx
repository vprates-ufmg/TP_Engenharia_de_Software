import React, { useState, useEffect } from "react";

import "../Styles/Select.css"

const CaixaDisciplinas = _ => {
  const [disciplinas, setDisciplinas] = useState([]);

  useEffect(() => {
    async function fetchDisciplinas() {
      const response = await fetch("http://127.0.0.1:5000/fetch_disciplinas", {
        method: "GET",
      });

      const data = await response.json();
      setDisciplinas(data.data);
      console.log(disciplinas)
    }
    fetchDisciplinas();
  }, []);

  return (
    <select className="custom-select" defaultValue="Selecione uma Disciplina">
      {disciplinas.map((disciplina) => (
        <option className="custom-option" value={disciplina.id}>{disciplina.nome}</option>
      ))}
    </select>
  );
}

export default CaixaDisciplinas;
