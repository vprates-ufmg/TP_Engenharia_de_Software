import React, { useState } from "react";
import Cookies from "js-cookie"

import "../Styles/WriteReview.css"
import "../Styles/TextBox.css"
import "../Styles/SendReview.css"

const WriteReview = props => {

    const session = Cookies.get("session");

    let review = {
        "semester": props.semester,
        "teacher_id": props.teacher_id,
        "disciplina_id": props.disciplina_id,
        "is_anonymous": true,
        "content": "",
        "session": session,
    }

    const [content, setContent] = useState('')
    const [anonymous, setAnonymous] = useState(true)

    const handleContentChange = event => {
        // 👇️ access textarea value
        setContent(event.target.value);
    };

    const handleAnonymous = _ => {
        setAnonymous(anonymous => !anonymous)
    }

    async function createReview() {
        const headers = new Headers();
        review.content = content
        review.is_anonymous = anonymous
        review.session = session
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

    return (
        <div className="write-review">
            <div className="text-box">
                <textarea className="text-review" name="review" id="review" cols="30" rows="5"
                    placeholder="Escreva sua Review!" value={content}
                    onChange={handleContentChange}
                ></textarea>
            </div>
            <div className="send-review">
                <div className="toggle-review">
                    <label className="switch">
                        <input type="checkbox" defaultChecked={anonymous} onClick={handleAnonymous} />
                        <span className="slider round"></span>
                    </label>
                    <p>Enviar Anônimo?</p>
                </div>
                <button onClick={createReview}>Enviar Review</button>
            </div>
        </div>
    )
}

export default WriteReview