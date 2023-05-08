import React, { useState, useEffect } from "react";

import "../Styles/Select.css"

const CaixaSemestres = _ => {
  const [semestres, setSemestres] = useState([]);

  useEffect(() => {
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
    setSemestres(data.data)
    console.log(data)
  }
  fetchSemestres()
  },[]);

    return (
      <select className="custom-select" defaultValue="Selecione um Semestre">
        {semestres.map((item) => (
          <option className="custom-option" value={item.nome} key={item.nome}>{item.nome}</option>
        ))}
      </select>
    );
  }
export default CaixaSemestres