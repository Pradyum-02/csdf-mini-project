import React from 'react';
import { Card } from '../components/Card';
import { Button } from '../components/Button';

const Reports: React.FC = () => {
  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold text-gray-900">
        Reports
      </h1>
      
      <Card>
        <h2 className="mb-4 text-xl font-semibold text-gray-900">
          Generated Reports
        </h2>
        <p className="text-gray-600">
          List of generated forensic reports would be displayed here.
        </p>
        <Button variant="outline" onClick={() => { /* Generate new report */ }}>
          Generate New Report
        </Button>
      </Card>
    </div>
  );
};

export default Reports;
