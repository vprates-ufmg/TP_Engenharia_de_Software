import React, { useState } from "react";

import Hash from "../../Services/hash";
import api from "../../Services/api";

import LoginIcon from "../../Images/login-icon.png"

import '../../Styles/Forms.css'

const Login = props => {
    const [user, setUser] = useState(null)
    const [password, setPassword] = useState(null)
    const [passwordShown, setPasswordShown] = useState(false);

    const togglePassword = () => {
        setPasswordShown(!passwordShown)
    }

    const handleLogin = e => {
        e.preventDefault()
        const password_hash = Hash(password)
        api.post('/login', {
            username: user,
            password_hash: password_hash
        })
            .then(
                response => {
                    console.log(response)
                }
            )
    }

    return (
        <div className="wrapper">
            <div className="form-box">
                <div className="header">
                    <img src={LoginIcon} alt="Ícone de Login" />
                    <p>Profs' Review - Login</p>
                </div>
                <div className="form-body">

                    <form onSubmit={handleLogin}
                        className='form'
                        id="form"
                        method="POST">

                        <input onChange={(e) => setUser(e.target.value)}
                            type="text"
                            name="username"
                            id="username"
                            placeholder="Digite seu usuário"
                            minLength={4}
                            required></input>

                        <div className="password-line">
                            <input
                                onChange={(e) => setPassword(e.target.value)}
                                type={passwordShown ? "text" : "password"}
                                name="password"
                                id="password"
                                placeholder="Digite sua senha"
                                minLength={6} required></input>
                            <i onClick={togglePassword}
                                className={passwordShown ? "far fa-eye-slash" : "far fa-eye"}
                                id="toggle-password"></i>
                        </div>
                        <input type="hidden"
                            name="password_hash"
                            id="password-hash"
                        ></input>

                        <button className='form-button' type="submit">Login</button>
                        <p>Não possui conta? <a href="/register">Registre-se</a> agora</p>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Login
