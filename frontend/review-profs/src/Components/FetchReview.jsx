import React, { useEffect, useState } from "react";

import SortingMethod from "./SortingMethod"

import "../Styles/FetchReview.css"

const FetchReview = _ => {

  const items = [
    {
      review_id: 1,
      autor: "John Smith",
      semester: "Fall 2022",
      professor: "Dr. Jane Doe",
      disciplina: "Introduction to Computer Science",
      time: "2022-10-01 14:30:00",
      votes: 10,
      content:
        "Dr. Jane Doe is an amazing professor! She explains concepts very clearly and is always willing to answer questions. The assignments were challenging but rewarding. I highly recommend this course.",
    },
    {
      review_id: 2,
      autor: "Jane Johnson",
      semester: "Spring 2022",
      professor: "Dr. John Smith",
      disciplina: "Advanced Calculus",
      time: "2022-03-15 09:00:00",
      votes: 5,
      content:
        "Dr. John Smith is a great professor! He is very knowledgeable and passionate about the subject. The lectures were engaging and the homework was fair. I learned a lot in this course.",
    },
    {
      review_id: 3,
      autor: "Bob Brown",
      semester: "Fall 2021",
      professor: "Dr. Alice Green",
      disciplina: "Intro to Psychology",
      time: "2021-11-10 16:45:00",
      votes: 2,
      content:
        "Dr. Alice Green is a good professor, but the course was not very interesting. The material was presented in a dry and unengaging way. The exams were fair, but I didn't feel like I learned much.",
    },
    {
      review_id: 4,
      autor: "Bob Brown",
      semester: "Fall 2021",
      professor: "Dr. Alice Green",
      disciplina: "Intro to Psychology",
      time: "2021-11-10 16:45:00",
      votes: 2,
      content:
        "Dr. Alice Green is a good professor, but the course was not very interesting. The material was presented in a dry and unengaging way. The exams were fair, but I didn't feel like I learned much.",
    },
  ];

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
    <div className="relative">
      <div className="sort-by"><SortingMethod></SortingMethod></div>
      {items.map((item) => (
        <div className="reviews" id={item.review_id}>
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