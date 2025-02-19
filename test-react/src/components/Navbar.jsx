import React from 'react'
import { Link } from 'react-router-dom'
import './Components.css'


function Navbar() {
    return(
        <>
        <nav className="navbarContainer">
            <Link className="navLinks" to="/api/voli">Voli</Link>
            <Link className="navLinks" to="/api/compagnie_voli">Compagnie</Link>
            <Link className="navLinks" to="/api/aeroporti">Aereoporti</Link>
        </nav>
        </>
    )
}

export default Navbar;
