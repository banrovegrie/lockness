import React from 'react';
import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  return (
    <div style={{ /* Styles for your container */ }}>
      <button style={{ /* Styles for your button */ }}>
        I want to train a model
      </button>
      <button onClick={() => navigate('/upload-data')} style={{ /* Styles for your button */ }}>
        I want to sell my data
      </button>
    </div>
  );
}

export default Home;
