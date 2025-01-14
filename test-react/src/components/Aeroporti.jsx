import axios from 'axios';
import { useState, useEffect } from 'react';

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
      <h2>Aeroporti che effettuano voli</h2>
      <table border="4">
        <thead>
          <tr>
            <th>Codice Aeroporto</th>
            <th>Aeroporto</th>
          </tr>
        </thead>
        <tbody>
          {dati.map((item, index) => (
            <tr key={index}>
              <td>{item[0]}</td>
              <td>{item[1]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Aeroporti;
