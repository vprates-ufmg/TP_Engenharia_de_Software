import React, { useState } from "react";

import Sidebar from "../Components/Sidebar";

import '../Styles/Home.css'

const Home = _ => {

    return (
        <div className="wrapper">
            <div className="sidebar">
                <Sidebar />
            </div>

        </div>
    )
}

export default Home
