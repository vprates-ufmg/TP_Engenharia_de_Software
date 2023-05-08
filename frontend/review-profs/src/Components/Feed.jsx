import React from "react";

import "../Styles/Feed.css"

import WriteReview from "./WriteReview";

const Feed = _ => {

    return (
        <div className="feed">
            <h1>Página Inicial</h1>
            <hr />
            <WriteReview></WriteReview>
            <h1>Reviews de Profs</h1>
            <hr />
        </div>
    )
}

export default Feed