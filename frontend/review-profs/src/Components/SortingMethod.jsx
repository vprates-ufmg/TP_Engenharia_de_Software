import React from "react";

const SortingMethod = _ => {
    const sorting = [
        "Mais Novos",
        "Mais Antigos",
        "Melhores Avaliados",
        "Piores Avaliados",

    ]
  return (
    <select className="sort-by custom-select" defaultValue="Selecione uma Disciplina">
      {sorting.map((item) => (
        <option className="custom-option" value={item}>{item}</option>
      ))}
    </select>
  );
}

export default SortingMethod;
