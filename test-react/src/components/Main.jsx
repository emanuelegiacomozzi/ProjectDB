import axios from 'axios'
import {useState, useEffect} from 'react'

function Main({tipo}){
    const [dati, setDati] = useState([])
    const [errore, setError] = useState(null)

    const apiUrl = {
        voli: 'http://localhost:5002/api/voli',
        compagnie_voli: 'http://localhost:5002/api/compagnie_voli',
        aeroporti: 'http://localhost:5002/api/aeroporti',
        aeroporti_arr_part: 'http://localhost:5002/api/aeroporti_arr_part',
        luogo_aeroporti: 'http://localhost:5002/api/luogo_aeroporti'
    }

    useEffect(() => {
        if (!apiUrl[tipo]) return; // Se l'URL non è valido, non fare nulla
    
        const fetchDati = async () => {
          try {
            const response = await axios.get(apiUrl[tipo])
            setDati(response.data)
          } catch (err)  {
            console.error('Errore nel recupero dei dati: ', err)
            setError('Errore nel recupero dei dati')
          }
        };
    
        fetchDati();
      }, [tipo]);

      if (errore) {
        return <div>{errore}</div>;
      }
    
    return(
        <div>
            
      <h2>Risultati</h2>
      <table border="2">
        <thead>
            <tr>
                <th>Codice</th>
                <th>Compagnia</th>
                <th>Durata</th>
            </tr>
        </thead>
        <tbody>
          {dati.map((item, index) => (
            <tr key={index}>
              <td>{item[0]}</td>
              <td>{item[1]}</td>
              <td>{item[2] || 'NULL'}</td>
            </tr>
          ))}
      </tbody>
      </table>
    </div>
    )
}

export default Main;