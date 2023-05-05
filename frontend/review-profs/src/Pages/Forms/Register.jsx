import React, { useState } from "react";

import api from "../../Services/api";
import Hash from "../../Services/hash";

import RegisterIcon from "../../Images/register-icon.png"

import '../../Styles/Forms.css'

const Login = _ => {
    const [user, setUser] = useState(null)
    const [password, setPassword] = useState(null)
    const [passwordShown, setPasswordShown] = useState(false);

    const togglePassword = () => {
        setPasswordShown(!passwordShown)
    }

    const handleSubmit = async e => {
        e.preventDefault()
        try {
            const password_hash = Hash(password)
            api.post('/register', { data: JSON.stringify({
                username: user,
                password_hash: password_hash
            }),
         })
        } catch(error) {
            console.error(error)
        }
    }

    return (
        <div className="wrapper">
            <div className="form-box">
                <div className="header">
                    <img src={RegisterIcon} alt="Ícone de Registro" />
                    <p>Profs' Review - Registro</p>
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
                            placeholder="Escolha seu usuário"
                            minLength={4}
                            required></input>

                        <div className="password-line">
                            <input
                                onChange={(e) => setPassword(e.target.value)}
                                type={passwordShown ? "text" : "password"}
                                name="password"
                                id="password"
                                placeholder="Escolha sua senha"
                                minLength={6} required></input>
                            <i onClick={togglePassword}
                                className={passwordShown ? "far fa-eye-slash" : "far fa-eye"}
                                id="toggle-password"></i>
                        </div>
                        <button className='form-button' type="submit">Cadastre-se</button>
                        <p>Já possui conta? <a href="/login">Faça Login</a> agora</p>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Login
