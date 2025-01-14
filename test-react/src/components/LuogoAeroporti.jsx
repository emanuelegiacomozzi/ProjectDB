import axios from 'axios';
import { useState, useEffect } from 'react';

function LuogoAeroporti() {
  const [dati, setDati] = useState([]);
  const [errore, setError] = useState(null);

  useEffect(() => {
    const fetchDati = async () => {
      try {
        const response = await axios.get('http://localhost:5002/api/luogo_aeroporti');
        setDati(response.data);
      } catch (err) {
        console.error('Errore nel recupero dei dati: ', err);
        setError('Errore nel recupero dei dati');
      }
    };

    fetchDati();
  }, []);

  if (errore) {
    return <div>{errore}</div>;
  }

  return (
    <div>
      <h2>Luogo degli aeroporti</h2>
      <table border="4">
        <thead>
          <tr>
            <th>Codice Aeroporto</th>
            <th>Città</th>
            <th>Nazione</th>
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
  );
}

export default LuogoAeroporti;
