import React, { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import Cookies from "js-cookie";

import '../Styles/Home.css'
import "../Styles/Feed.css"
import "../Styles/Sidebar.css"
import "../Styles/Select.css"

import WriteReview from "../Components/WriteReview";
import FetchReview from "../Components/FetchReview";
import Logout from "../Components/Logout";

const Home = _ => {
    const navigate = useNavigate();
    var session = Cookies.get("session")
    if (session === undefined){
        session = "";
    }

    useEffect(() => {
        async function verificarSessao() {
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        const response = await fetch('http://127.0.0.1:5000/verifica_sessao', {
            method: 'POST',
            headers: headers,
            body: JSON.stringify({session: session})
        })

        const data = await response.json()
          if (!data.success) {
            navigate("/login")
          }
        }
        verificarSessao();
      }, [navigate, session]);


    const [disciplinas, setDisciplinas] = useState([]);
    const [professores, setProfessores] = useState([]);
    const [semestres, setSemestres] = useState([]);

    const [disciplineValue, setDisciplineValue] = useState(1);
    const [professorValue, setProfessorValue] = useState(1); 
    const [semestreValue, setSemestreValue] = useState(1); 

    useEffect(() => {
        async function fetchDisciplinas() {
            const response = await fetch("http://127.0.0.1:5000/fetch_disciplinas", {
                method: "GET",
            });

            const data = await response.json();
            setDisciplinas([{"id": 0, nome: ""}].concat(data.data));
        }
        async function fetchProfessores(id_disciplina = "") {
            const headers = new Headers();
            headers.append("Content-Type", "application/json");
            const response = await fetch("http://127.0.0.1:5000/fetch_professores", {
                method: "POST",
                headers: headers,
                body: JSON.stringify({ disciplina_id: id_disciplina }),
            });

            const data = await response.json();
            setProfessores([{"id": 0, nome: ""}].concat(data.data))
        }
        async function fetchSemestres(id_disciplina = "", id_professor = "") {
            const headers = new Headers();
            headers.append("Content-Type", "application/json");
            const response = await fetch("http://127.0.0.1:5000/fetch_semestres", {
                method: "POST",
                headers: headers,
                body: JSON.stringify({
                    disciplina_id: id_disciplina,
                    professor_id: id_professor,
                }),
            });

            const data = await response.json();
            setSemestres([{"id": 0, nome: ""}].concat(data.data))
        }
        fetchDisciplinas()
        fetchProfessores()
        fetchSemestres()
    }, []);


    return (
        <div className="wrapper">
            <div className="sidebar">
                <div className="header">
                    <div className="header-container">
                        <h2>Disciplina:</h2>
                        <hr />
                        <select className="custom-select" value={disciplineValue} onChange={e => setDisciplineValue(e.target.value)}>
                            {disciplinas.map((disciplina) => (
                                <option className="custom-option" value={disciplina.id} key={disciplina.id}>{disciplina.nome}</option>
                            ))}
                        </select>
                        <h2>Professor:</h2>
                        <hr />
                        <select className="custom-select" value={professorValue} onChange={e => setProfessorValue(e.target.value)}>
                            {professores.map((item) => (
                                <option className="custom-option" value={item.id} key={item.id}>{item.nome}</option>
                            ))}
                        </select>
                        <h2>Semestre:</h2>
                        <hr />
                        <select className="custom-select" value={semestreValue} onChange={e => setSemestreValue(e.target.value)}>
                            {semestres.map((item) => (
                                <option className="custom-option" value={item.nome} key={item.nome}>{item.nome}</option>
                            ))}
                        </select>
                    </div>
                </div>
                <div className="bottom">
                    <Logout />
                </div>
            </div>
            <div className="feed">
                <h1>Página Inicial</h1>
                <hr />
                <WriteReview
                    teacher_id={professorValue}
                    disciplina_id={disciplineValue}
                    semester={semestreValue}
                    />
                <h1>Reviews de Profs</h1>
                <hr />
                <FetchReview></FetchReview>
            </div>
        </div>
    )
}

export default Home
