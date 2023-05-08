import React, { useEffect, useState } from "react";
import Cookies from "js-cookie"

import "../Styles/FetchReview.css"

const FetchReview = _ => {

  const [reviews, setReviews] = useState([]);

  let [selectedIndex, setSelectedIndex] = useState(0);
  
    const options =[
      { value: "0", label: "Mais Novos" },
      { value: "1", label: "Mais Antigos" },
      { value: "2", label: "Melhores Avaliados" },
      { value: "3", label: "Piores Avaliados" }
    ]

  const handleSelectChange = event => {
    setSelectedIndex(parseInt(event.target.value));
  };

  const session = Cookies.get('session')
  async function handleUpvote(id) {
    const headers = new Headers();
    headers.append("Content-Type", "application/json");
    const response = await fetch("http://127.0.0.1:5000/upvote_review", {
        method: "POST",
        headers: headers,
        body: JSON.stringify({
          session: session,
          review_id: id,
        }),
      });
      let data = await response.json()
      if(data.success) {
        alert(data.message)
        window.location.reload(true)
      }
      else {
        alert(data.message)
      }
  }

  async function handleDownvote(id) {
    const headers = new Headers();
    headers.append("Content-Type", "application/json");
    const response = await fetch("http://127.0.0.1:5000/downvote_review", {
        method: "POST",
        headers: headers,
        body: JSON.stringify({
          session: session,
          review_id: id,
        }),
      });
      let data = await response.json()
      if(data.success) {
        alert(data.message)
        window.location.reload(true)
      }
      else {
        alert(data.message)
      }
  }
  
  useEffect(() => {
    async function fetchReview() {
      const headers = new Headers();
      let body = JSON.stringify({
        "sorting": selectedIndex,
      })
      headers.append("Content-Type", "application/json");
      const response = await fetch("http://127.0.0.1:5000/fetch_review", {
        method: "POST",
        headers: headers,
        body: JSON.stringify({
          "sorting": selectedIndex,
        }),
      });

      let data = await response.json();
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
        <p>Odernar por:</p>
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
              <button type="button" onClick={() => handleUpvote(item.review_id)}>↑</button>
              {item.votes}
              <button type="button" className="down-vote" onClick={() => handleDownvote(item.review_id)}>↓</button>
            </div>
          </div>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default FetchReview