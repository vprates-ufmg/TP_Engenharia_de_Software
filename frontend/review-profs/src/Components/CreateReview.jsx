import React, { useEffect } from "react";

const CreateReview = props => {
  useEffect(() => {
    async function createReview() {
      let review = {
        "semester": "2021/2",
        "teacher_id": 'df90e7ba-23ce-4b5a-85a6-2600217503b4',
        "disciplina_id": '633e1d46-6fb7-43d3-a17c-34a517729c26',
        "is_anonymous": true,
        "content": "muito bom o professor, mas no maximo 500 caracteres",
        "session": "2a5b156a-0292-4151-a07c-6a4b7aeea423"
      }
      const headers = new Headers();
      headers.append("Content-Type", "application/json");
      const response = await fetch("http://127.0.0.1:5000/create_review", {
        method: "POST",
        headers: headers,
        body: JSON.stringify(review),
      });
      let data = await response.json()
      console.log(data)
    }
    createReview()
  }, []);

  return (
    <>
        {alert("Review criada com sucesso")}
    </>
  );
}

export default CreateReview