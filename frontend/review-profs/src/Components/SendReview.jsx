import React from "react";

import "../Styles/SendReview.css"

const SendReview = _ => {

    return (
        <div className="send-review">
            <div className="toggle-review">
                <label className="switch">
                    <input type="checkbox" />
                    <span className="slider round"></span>
                </label>
                <p>Enviar Anônimo?</p>
            </div>
            <button>Enviar Review</button>
        </div>
    )
}

export default SendReview