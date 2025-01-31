import React from 'react'
import { Link } from 'react-router-dom'
import './Components.css'

function Header() {
  return (
    <header>
      <h1>Agenzia di viaggi</h1>
      <nav>
          <Link className="navLink" to="/api/voli">Voli</Link>
          <Link className="navLink" to="/api/compagnie_voli">Compagnie</Link>
          <Link className="navLink" to="/api/aeroporti">Aereoporti</Link>
          <Link className="navLink" to="/api/aeroporti_arr_part">Aereoporti di partenza e arrivo</Link>
          <Link className="navLink" to="/api/luogo_aeroporti">Luogo aereoporto</Link>
      </nav>
    </header>
  )
}

export default Header