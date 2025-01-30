import './App.css'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Voli from './components/Voli'
import { Link } from 'react-router-dom'
import Compagnie from './components/Compagnie'
import Aeroporti from './components/Aeroporti'
import Arr_Part from './components/Arr_Part'
import LuogoAeroporti from './components/LuogoAeroporti'




function App() {

  return (
    <>
    <Router>
    <div className='pageContainer'>
    <header style={{ textAlign: 'center', backgroundColor: '#f8f8f8', padding: '20px' , position:'static'}}>
          <h1>Agenzia di viaggi</h1>
          <nav>
              <ul className='navList'>
                <li><Link to="/api/voli">Visualizza voli disponibili</Link></li>
                <li><Link to="/api/compagnie_voli">Visualizza voli delle rispettive compagnie</Link></li>
                <li><Link to="/api/aeroporti">Visualizza aeroporti che effettuano voli</Link></li>
                <li><Link to="/api/aeroporti_arr_part">Visualizza aeroporti di partenza e arrivo</Link></li>
                <li><Link to="/api/luogo_aeroporti">Visualizza luogo degli aeroporti</Link></li>
              </ul>
            </nav>
    </header>
    <main style={{ flex: 1, padding: '20px', position:'static'}}>
          <Routes>
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
