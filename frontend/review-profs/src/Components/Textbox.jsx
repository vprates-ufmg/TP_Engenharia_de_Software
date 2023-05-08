import React from "react";

import "../Styles/TextBox.css"

const TextBox = _ => {

    return (
        <div className="text-box">
            <textarea className="text-review" name="review" id="review" cols="30" rows="5"
                placeholder="Escreva sua Review!"></textarea>
        </div>
    )
}

export default TextBox