import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Buy from './Pages/buy'
import Login from './Pages/login'
import Main from './Pages/main';
import Delay from './Pages/delay';

function App() {
  return (
    <BrowserRouter basename='/'>
      <Routes>
        <Route path='/' exact element={<Main />}></Route>
        <Route path='/buy' exact element={<Buy />}></Route>
        <Route path='/login' exact element={<Login />}></Route>
        <Route path='/delay' exact element={<Delay />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
