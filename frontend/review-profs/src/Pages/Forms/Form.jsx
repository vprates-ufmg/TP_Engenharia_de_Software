import React, { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import Cookies from "js-cookie";

import Hash from "../../Services/Hash";

import '../../Styles/Forms.css'

const Form = props => {
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
          if (data.success) {
            navigate("/feed")
          }
        }
        verificarSessao();
      }, [navigate, session]);

    
    const [user, setUser] = useState(null)
    const [password, setPassword] = useState(null)
    const [passwordShown, setPasswordShown] = useState(false);

    const togglePassword = () => {
        setPasswordShown(!passwordShown)
    }

    
    async function handleSubmit(e) {
        var session = Cookies.get("session")
        if (session === undefined){
          session = "";
        }

        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        e.preventDefault()
        const password_hash = await Hash(password)
        const response = await fetch(props.url, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify({ session: session, username: user, password_hash })
        })

        const data = await response.json()

        if (data.success) {
            Cookies.set("session", data.session);
        }
        alert(data.message)
        navigate("/feed")
    }

    return (
        <div className="form-wrapper">
            <div className="form-box">
                <div className="form-header">
                    <img src={props.image} alt={props.imageAlt} />
                    <p>Profs' Review - {props.pageType}</p>
                </div>
                <div className="form-body">

                    <form onSubmit={handleSubmit}
                        className='form'
                        id="form"
                        method="POST">

                        <input onChange={(e) => setUser(e.target.value)}
                            type="text"
                            name="username"
                            id="username"
                            placeholder={props.userPlaceholder}
                            minLength={4}
                            required></input>

                        <div className="password-line">
                            <input
                                onChange={(e) => setPassword(e.target.value)}
                                type={passwordShown ? "text" : "password"}
                                name="password"
                                id="password"
                                placeholder={props.passwordPlaceholder}
                                minLength={6} required></input>
                            <i onClick={togglePassword}
                                className={passwordShown ? "far fa-eye-slash" : "far fa-eye"}
                                id="toggle-password"></i>
                        </div>
                        <button className='form-button' type="submit">{props.buttonText}</button>
                        <p>{props.pText} <a href={props.refferLink}>{props.aText}</a> agora</p>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Form
