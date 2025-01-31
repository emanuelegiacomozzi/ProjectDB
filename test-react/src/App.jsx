import './App.css'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Voli from './components/Voli'
import { Link } from 'react-router-dom'
import Compagnie from './components/Compagnie'
import Aeroporti from './components/Aeroporti'
import Arr_Part from './components/Arr_Part'
import LuogoAeroporti from './components/LuogoAeroporti'
import Header from './components/Header'
import Home from './components/Home'


function App() {

  return (
    <>
    <Router>
    <div className='pageContainer'>
    <Header/>
    <main className='mainApp'>
          <Routes>
          <Route path="/" element={<Home />} /> 
            <Route path="/api/voli" element={<Voli/>}></Route>
            <Route path="/api/compagnie_voli" element={<Compagnie/>}></Route>
            <Route path="/api/aeroporti" element={<Aeroporti/>}></Route>
            <Route path="/api/aeroporti_arr_part" element={<Arr_Part/>}></Route>
            <Route path="/api/luogo_aeroporti" element={<LuogoAeroporti/>}></Route>
          </Routes>
      </main>
      <footer className='footerClass'>
        <p>&copy; 2025 Agenzia di Viaggi. Tutti i diritti riservati.</p>
      </footer>
      </div>
      </Router>
    </>
  )
}

export default App
