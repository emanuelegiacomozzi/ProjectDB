import axios from 'axios';
import { useState, useEffect } from 'react';
import './Table.css'


function Aeroporti() {
  const [dati, setDati] = useState([]);
  const [errore, setError] = useState(null);

  useEffect(() => {
    const fetchDati = async () => {
      try {
        const response = await axios.get('http://localhost:5002/api/aeroporti');
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
      <table className="Table">
        <thead>
          <tr>
            <th>Aeroporto</th>
            <th>Codice</th>
            <th>Città</th>
            <th>Nazione</th>
          </tr>
        </thead>
        <tbody>
          {dati.map((item, index) => (
            <tr key={index}>
              <td>{item[1]}</td>
              <td>{item[0]}</td>
              <td>{item[2]}</td>
              <td>{item[3]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Aeroporti;
