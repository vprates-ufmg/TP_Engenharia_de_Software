import React, { useEffect, useState } from "react";

import SortingMethod from "./SortingMethod"

import "../Styles/FetchReview.css"

const FetchReview = _ => {

  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    async function fetchReview() {
      const headers = new Headers();
      headers.append("Content-Type", "application/json");
      const response = await fetch("http://127.0.0.1:5000/fetch_review", {
        method: "POST",
        headers: headers,
        body: JSON.stringify({
          "sorting": 0,
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
    <div className="relative">
      <div className="sort-by"><SortingMethod></SortingMethod></div>
      {reviews.map((item) => (
        <div className="reviews" key={item.review_id}>
          <div className="author-row">
            <div className="author">Autor: {item.autor}</div>
          </div>
          <hr />
          <div className="class-taken author-row">
            Turma: {item.disciplina} | {item.professor} | {item.semester}
          </div>
          <div className="review-body">
            {item.content}
          </div>
          <div className="bottom-review">
            <p>@review feito em {item.time}</p>
            <div>
              <button>↑</button>
              {item.votes}
            </div>
          </div>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default FetchReview