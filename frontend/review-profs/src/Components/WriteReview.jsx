import React from "react";

import "../Styles/WriteReview.css"

import TextBox from "./Textbox";
import SendReview from "./SendReview";

const WriteReview = _ => {

    return (
        <div className="write-review">
            <TextBox></TextBox>
            <SendReview></SendReview>
        </div>
    )
}

export default WriteReview