import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [origen, setOrigen] = useState('');
  const [destino, setDestino] = useState('');
  const [fecha, setFecha] = useState('');
  const [vuelos, setVuelos] = useState([]);

  const buscarVuelos = async () => {
    const response = await axios.get(`http://localhost:8000/buscar`, {
      params: { origen, destino, fecha }
    });
    setVuelos(response.data.vuelos);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Comparador de Vuelos</h1>
      <input placeholder="Origen" value={origen} onChange={(e) => setOrigen(e.target.value)} />
      <input placeholder="Destino" value={destino} onChange={(e) => setDestino(e.target.value)} />
      <input placeholder="Fecha" value={fecha} onChange={(e) => setFecha(e.target.value)} type="date" />
      <button onClick={buscarVuelos}>Buscar</button>

      <h2>Resultados:</h2>
      <ul>
        {vuelos.map((vuelo, index) => (
          <li key={index}>
            {vuelo.proveedor} - {vuelo.origen} ➔ {vuelo.destino} - {vuelo.precio}€
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
