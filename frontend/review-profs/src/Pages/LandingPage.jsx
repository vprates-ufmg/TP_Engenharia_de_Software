import React from 'react'
import '../Styles/LandingPage.css'
import { Link } from 'react-router-dom';

const LandingPage = () => {
  return (
    <div>

    <nav> 
      <ul className='header'>
        <li>ReviewProfs</li>
        <li><Link to="/" className='login'>Log in</Link></li>
      </ul>
    </nav>
    <div className='main-container'>

    <h1>Estudante da UFMG?<br/>
Não faça sua matrícula no escuro</h1>

<div className="keypoints">
  <li>
    👉  Avalie seus professores
  </li>
  <li>
    👉  Interaja com outros estudantes
  </li>

  <li>
    👉  Escreva reviews das disciplinas
  </li>
</div>

<Link to="/register" className="register"> Registre-se agora! </Link>
</div>
    </div>
  )
};

export default LandingPage