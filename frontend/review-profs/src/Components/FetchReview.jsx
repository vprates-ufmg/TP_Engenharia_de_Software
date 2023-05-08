import React, { useEffect, useState } from "react";

const FetchReview = _ => {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    async function fetchReview(
      sorting = 1,
    ) {
      const headers = new Headers();
      headers.append("Content-Type", "application/json");
      const response = await fetch("http://127.0.0.1:5000/fetch_review", {
        method: "POST",
        headers: headers,
        body: JSON.stringify({
          sorting: 1,
        }),
      });

      let data = await response.json();
      console.log(response)
      console.log(data)
      if (!data.success) {
        alert(data.message);
        return;
      }
      setReviews(data.data)
    }
    fetchReview()
  }, []);

  return (
    <ul>
      {reviews.map((item) => (
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

export default FetchReview