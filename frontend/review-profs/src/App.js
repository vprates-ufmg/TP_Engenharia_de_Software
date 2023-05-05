import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Login from './Pages/Forms/Login'
import Register from './Pages/Forms/Register'

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path='/' element={< Login />} />
        <Route exact path='/login' element={< Login />} />
        <Route exact path='/register' element={< Register />} />
      </Routes>
    </Router>
  )
}

export default App;