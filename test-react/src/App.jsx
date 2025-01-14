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
    <fieldset style={{backgroundColor:"white"}}>
    <div className="team-table">
          <h1>Agenzia di viaggi</h1>
            <fieldset style={{border:"2px solid black", paddingLeft:"10px", paddingTop:"20px", paddingRight:"10px",paddingBottom:"10px"}}>
            <legend style={{textAlign:"center", width:"auto", padding:"0 10px", backgroundColor:"white",display:"inline-block"}}>Operazioni disponibili</legend>
            <nav>
              <ul>
                <li><Link to="/api/voli">Visualizza voli disponibili</Link></li>
                <li><Link to="/api/compagnie_voli">Visualizza voli delle rispettive compagnie</Link></li>
                <li><Link to="/api/aeroporti">Visualizza aeroporti che effettuano voli</Link></li>
                <li><Link to="/api/aeroporti_arr_part">Visualizza aeroporti di partenza e arrivo</Link></li>
                <li><Link to="/api/luogo_aeroporti">Visualizza luogo degli aeroporti</Link></li>
              </ul>
            </nav>
            </fieldset>
          <Routes>
            <Route path="/api/voli" element={<Voli/>}></Route>
            <Route path="/api/compagnie_voli" element={<Compagnie/>}></Route>
            <Route path="/api/aeroporti" element={<Aeroporti/>}></Route>
            <Route path="/api/aeroporti_arr_part" element={<Arr_Part/>}></Route>
            <Route path="/api/luogo_aeroporti" element={<LuogoAeroporti/>}></Route>
          </Routes>
      </div>
      </fieldset>
      </Router>
    </>
  )
}

export default App
