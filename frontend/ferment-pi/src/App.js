import React from 'react';
import './App.css';
import LastTemp from './features/temperature/LastTemp';

function App() {
  return (
    <div className="App">
      <h1>Ferment Pi</h1>
      <LastTemp />
    </div>
  );
}

export default App;
