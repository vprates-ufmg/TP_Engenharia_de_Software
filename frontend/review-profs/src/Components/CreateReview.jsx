import React, { useEffect } from "react";

const CreateReview = props => {
  useEffect(() => {
    async function createReview() {
      let review = {
        "semester": "2021/2",
        "teacher_id": "120526b0-9a0a-498c-acae-8d25a98d03e1",
        "disciplina_id": "f0fc331b-1bb7-4978-91c6-ffff45141658",
        "is_anonymous": false,
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