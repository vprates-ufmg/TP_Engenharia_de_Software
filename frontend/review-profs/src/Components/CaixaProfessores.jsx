import React, { useState, useEffect } from "react";

import "../Styles/Select.css"

const CaixaProfessores = _ => {
  const [professores, setProfessores] = useState([]);

  useEffect(() => {
    async function fetchProfessores(id_disciplina = "") {
      const headers = new Headers();
      headers.append("Content-Type", "application/json");
      const response = await fetch("http://127.0.0.1:5000/fetch_professores", {
        method: "POST",
        headers: headers,
        body: JSON.stringify({ disciplina_id: id_disciplina }),
      });
      
      const data = await response.json();
      setProfessores(data.data)
      console.log(data.data)
    }
    fetchProfessores()
    },[]);

    return (
      <select className="custom-select" defaultValue="Selecione um(a) Professor(a)">
        {professores.map((item) => (
          <option className="custom-option" value={item.id} key={item.id}>{item.nome}</option>
        ))}
      </select>
    );
  }

export default CaixaProfessores
