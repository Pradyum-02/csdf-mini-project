import React from 'react';
import { Card } from '../components/Card';
import { Button } from '../components/Button';

const CaseDetail: React.FC = () => {
  return (
    <div>
      <div className="mb-6 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-gray-900">
          Case Details
        </h1>
        <div className="flex space-x-3">
          <Button variant="outline" onClick={() => { /* Edit case */ }}>
            Edit Case
          </Button>
          <Button variant="secondary" onClick={() => { /* Upload evidence */ }}>
            Upload Evidence
          </Button>
        </div>
      </div>
      
      <Card>
        <h2 className="mb-4 text-xl font-semibold text-gray-900">
          Case Information
        </h2>
        <p className="text-gray-600">
          Case details would be displayed here.
        </p>
      </Card>
      
      <Card>
        <h2 className="mb-4 text-xl font-semibold text-gray-900">
          Evidence in this Case
        </p className="text-gray-600">
          Evidence list would be displayed here.
        </p>
      </Card>
      
      <div className="mt-6">
        <Button variant="primary" onClick={() => { /* Generate report */ }}>
          Generate Forensic Report
        </Button>
      </div>
    </div>
  );
};

export default CaseDetail;
