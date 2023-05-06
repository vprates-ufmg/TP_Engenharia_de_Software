import React, { useState } from "react";

import Hash from "../../Services/Hash";
import Logout from "../../Services/Logout";

import '../../Styles/Forms.css'

const Form = props => {
    const [user, setUser] = useState(null)
    const [password, setPassword] = useState(null)
    const [passwordShown, setPasswordShown] = useState(false);

    const togglePassword = () => {
        setPasswordShown(!passwordShown)
    }

    async function handleSubmit(e) {
        e.preventDefault()
        const password_hash = await Hash(password)
        fetch(props.url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: user, password_hash })
        })

        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => alert(error));
    }

    return (
        <div className="wrapper">
            <div className="form-box">
                <div className="header">
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
            <button onClick={Logout}>Logout</button>

        </div>
    )
}

export default Form
