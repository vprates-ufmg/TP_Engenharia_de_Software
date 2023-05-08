import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import RegisterIcon from "./Images/register-icon.png";
import LoginIcon from "./Images/login-icon.png"

import Form from "./Pages/Forms/Form"
import CaixaDisciplinas from "./Components/CaixaDisciplinas"
import CaixaProfessores from "./Components/CaixaProfessores"
import CaixaSemestres from "./Components/CaixaSemestres"
import FetchReview from "./Components/FetchReview"
import CreateReview from "./Components/CreateReview"
import Home from "./Pages/Home"
import LandingPage from "./Pages/LandingPage"
function App() {
  return (
    <Router>
      <Routes>
      <Route exact path="/landingpage" element={<LandingPage/>} />
        <Route exact path='/' element={< Form
          pageType='Login'
          url='http://127.0.0.1:5000/login'
          image={LoginIcon}
          imageAlt="Ícone de Login"
          userPlaceholder="Digite seu usuário"
          passwordPlaceholder="Digite sua senha"
          refferLink="/register"
          buttonText="Login"
          pText="Ainda não possui conta? "
          aText="Cadastre-se"
          />} />
        <Route exact path='/login' element={< Form
          pageType='Login'
          url='http://127.0.0.1:5000/login'
          image={LoginIcon}
          imageAlt="Ícone de Login"
          userPlaceholder="Digite seu usuário"
          passwordPlaceholder="Digite sua senha"
          refferLink="/register"
          buttonText="Login"
          pText="Ainda não possui conta? "
          aText="Cadastre-se"
          />} />
        <Route exact path='/register' element={< Form
          pageType='Registro'
          url='http://127.0.0.1:5000/register'
          image={RegisterIcon}
          imageAlt="Ícone de Registro"
          userPlaceholder="Escolha seu usuário"
          passwordPlaceholder="Escolha sua senha"
          refferLink="/login"
          buttonText="Cadastre-se"
          pText="Já possui conta? "
          aText="Faça Login"
          />} />
          <Route exact path='/disciplinas' element={<CaixaDisciplinas></CaixaDisciplinas>}></Route>
          <Route exact path='/professores' element={<CaixaProfessores></CaixaProfessores>}></Route>
          <Route exact path='/semestres' element={<CaixaSemestres></CaixaSemestres>}></Route>
          <Route exact path='/home' element={<Home></Home>}></Route>
          <Route exact path='/create_review' element={<CreateReview></CreateReview>}></Route>
          <Route exact path='/fetch_review' element={<FetchReview></FetchReview>}></Route>
      </Routes>
    </Router>
  )
}

export default App;