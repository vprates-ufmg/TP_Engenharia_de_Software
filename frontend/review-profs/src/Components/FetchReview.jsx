import React, { useEffect, useState } from "react";
import Cookies from "js-cookie";

import "../Styles/FetchReview.css"

const FetchReview = _ => {

  const [reviews, setReviews] = useState([]);

  let [selectedIndex, setSelectedIndex] = useState(0);
  var session = Cookies.get("session")
    const options =[
      { value: "0", label: "Mais Novos" },
      { value: "1", label: "Mais Antigos" },
      { value: "2", label: "Melhores Avaliados" },
      { value: "3", label: "Piores Avaliados" }
    ]

  const handleSelectChange = event => {
    setSelectedIndex(parseInt(event.target.value));
  };
  const handleUpvoteClick = async (reviewId) => {
    const headers = new Headers();
    headers.append("Content-Type", "application/json");
    const response = await fetch("http://127.0.0.1:5000/upvote_review", {
      method: "POST",
      headers: headers,
      body: JSON.stringify({
        "review_id": reviewId,
        "session": session
      }),
    });
    let data = await response.json();
    console.log(response)
    console.log(data)
    if (!data.success) {
      alert(data.message);
      return;
    }
    const updatedReviews = reviews.map((review) => {
      if (review.review_id === reviewId) {
        return { ...review, votes: data.votes };
      } else {
        return review;
      }
    });
    setReviews(updatedReviews);
  };
  useEffect(() => {
    async function fetchReview() {
      const headers = new Headers();
      let body = JSON.stringify({
        "sorting": selectedIndex,
      })
      console.log(body)
      headers.append("Content-Type", "application/json");
      const response = await fetch("http://127.0.0.1:5000/fetch_review", {
        method: "POST",
        headers: headers,
        body: JSON.stringify({
          "sorting": selectedIndex,
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
  }, [selectedIndex]);

  return (
    <div className="relative">
      <div className="sort-by">
        <select className="sort-by custom-select" value={selectedIndex} onChange={handleSelectChange}>
          {options.map((option, index) => (
            <option className="custom-option" key={option.value} value={index}>{option.label}</option>
          ))}
        </select>
      </div>
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
              <button onClick={() => handleUpvoteClick(item.review_id)}>↑ {item.votes}</button>
            </div>
          </div>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default FetchReview
