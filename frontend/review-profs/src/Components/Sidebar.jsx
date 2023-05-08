import React from "react";

import CaixaDisciplinas from "./CaixaDisciplinas";
import CaixaProfessores from "./CaixaProfessores";
import CaixaSemestres from "./CaixaSemestres";
import Logout from "../Components/Logout";

import "../Styles/Sidebar.css"


const Sidebar = _ => {

    return (
        <div className="sidebar">
            <div className="header">
                <div className="header-container">
                    <h2>Disciplina:</h2>
                    <hr />
                    <CaixaDisciplinas />
                    <h2>Professor:</h2>
                    <hr />
                    <CaixaProfessores />
                    <h2>Semestre:</h2>
                    <hr />
                    <CaixaSemestres />
                </div>
            </div>
            <div className="bottom">
                <Logout />
            </div>
        </div>
    )
}

export default Sidebar