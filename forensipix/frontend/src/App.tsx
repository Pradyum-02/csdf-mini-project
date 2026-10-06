import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import './App.css';

// Pages
import Dashboard from './pages/Dashboard';
import Cases from './pages/Cases';
import CaseDetail from './pages/CaseDetail';
import EvidenceUpload from './pages/EvidenceUpload';
import EvidenceDetail from './pages/EvidenceDetail';
import EvidenceAnalysis from './pages/EvidenceAnalysis';
import Reports from './pages/Reports';
import Settings from './pages/Settings';

// Layouts
import MainLayout from './layouts/MainLayout';

function App() {
  return (
    <Router>
      <MainLayout>
        <Routes>
          <Route path="/" element={<Navigate replace to="/dashboard" />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/cases" element={<Cases />} />
          <Route path="/cases/new" element={<CaseDetail />}
          <Route path="/cases/:id" element={<CaseDetail />} />
          <Route path="/cases/:id/evidence/upload" element={<EvidenceUpload />} />
          <Route path="/evidence/:id" element={<EvidenceDetail />} />
          <Route path="/evidence/:id/analyze" element={<EvidenceAnalysis />} />
          <Route path="/reports" element={<Reports />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="*" element={<Navigate replace to="/dashboard" />} />
        </Routes>
      </MainLayout>
    </Router>
  );
}

export default App;
