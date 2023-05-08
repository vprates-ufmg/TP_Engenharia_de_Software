import React from "react";

import "../Styles/SendReview.css"

const SendReview = _ => {

    return (
        <div className="send-review">
            <div className="toggle-review">
                <label class="switch">
                    <input type="checkbox" />
                    <span class="slider round"></span>
                </label>
                <p>Enviar Anônimo?</p>
            </div>
            <button>Enviar Review</button>
        </div>
    )
}

export default SendReview