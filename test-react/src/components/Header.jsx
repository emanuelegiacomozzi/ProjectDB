import React from 'react'
import { Link } from 'react-router-dom'
import './Components.css'

function Header() {
  const imgUrl = "https://static.vecteezy.com/ti/vettori-gratis/p1/4185812-set-di-aereo-icona-nero-vettore-aereo-simbolo-set-gratuito-vettoriale.jpg"
  return (
    <header className="headerContainer">
      <div className="titleContainer">
        <h1 className="Agenzia">ViaggiaConNoi.it</h1>
        <img src={imgUrl} className="logo" />
      </div>
      <nav>
        <Link className="navLinks" to="/">Home Page</Link>
        </nav>
    </header>
  )
}

export default Header