import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './Home'; // Import Home component
import UploadDataPage from './UploadDataPage'; // Import UploadDataPage component

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} /> // Route for the Home page
      <Route path="/upload-data" element={<UploadDataPage />} /> // Route for the upload data page
    </Routes>
  );
}

export default App;
