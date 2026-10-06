import React from 'react';
import { Card } from '../components/Card';
import { Button } from '../components/Button';

const Settings: React.FC = () => {
  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold text-gray-900">
        Settings
      </h1>
      
      <Card>
        <h2 className="mb-4 text-xl font-semibold text-gray-900">
          General Settings
        </h2>
        <p className="text-gray-600">
          Application settings would be configured here.
        </p>
        <Button variant="outline" onClick={() => { /* Save settings */ }}>
          Save Settings
        </Button>
      </Card>
    </div>
  );
};

export default Settings;
