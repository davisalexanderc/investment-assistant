import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { CssBaseline } from '@mui/material';
import { DiscoveryPage } from './pages/DiscoveryPage';
import { LandingPage } from './pages/LandingPage';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <CssBaseline />
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/discover" element={<DiscoveryPage />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
