import React, { useState } from "react";

import Sidebar from "../Components/Sidebar";
import Feed from "../Components/Feed";

import '../Styles/Home.css'

const Home = _ => {

    return (
        <div className="wrapper">
            <Sidebar />
            <Feed />
        </div>
    )
}

export default Home
