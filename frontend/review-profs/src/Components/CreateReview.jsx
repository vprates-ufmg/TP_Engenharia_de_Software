import React, { useEffect } from "react";

const CreateReview = props => {
  useEffect(() => {
    async function createReview() {
      let review = {
        "semester": "2021/2",
        "teacher_id": 'df90e7ba-23ce-4b5a-85a6-2600217503b4',
        "disciplina_id": '633e1d46-6fb7-43d3-a17c-34a517729c26',
        "is_anonymous": true,
        "content": "Novo novo novo novo novo",
        "session": "b021f665-a40e-4f29-b373-8f3e693ce536"
      }
      const headers = new Headers();
      headers.append("Content-Type", "application/json");
      try {
        const response = await fetch("http://127.0.0.1:5000/create_review", {
          method: "POST",
          headers: headers,
          body: JSON.stringify(review),
        });
        let data = await response.json()
        alert(data.message)
      } catch (error) {
        alert(error.message);
      }
    }
    createReview()
  }, []);

  return (
    <>
      
    </>
  );
}

export default CreateReview
