import React, { useState, useEffect } from 'react';
import { Card } from '../components/Card';
import { Button } from '../components/Button';
import { Badge } from '../components/Badge';

const EvidenceDetail: React.FC = () => {
  const [evidence, setEvidence] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // In a real app, this would fetch data from the API
    // For now, we'll use mock data
    setTimeout(() => {
      setEvidence({
        id: 1,
        evidence_number: 'EVD-0001',
        original_filename: 'suspect.jpg',
        stored_filename: 'EVD-0001.jpg',
        file_size: 2457600,
        mime_type: 'image/jpeg',
        width: 1920,
        height: 1080,
        format: 'JPEG',
        sha256: '8f4c9a8e2b3d4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b',
        md5: 'a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6',
        upload_timestamp: '2026-10-07 02:10:00'
      });
      setLoading(false);
    }, 1000);
  }, []);

  if (loading) {
    return (
      <div className="p-8">
        <h1 className="mb-6 text-2xl font-bold text-gray-900">
          Evidence Details
        </h1>
        <div className="text-center py-12">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500"></div>
        </div>
      </div>
    );
  }

  if (!evidence) {
    return (
      <div className="p-8">
        <h1 className="mb-6 text-2xl font-bold text-gray-900">
          Evidence Not Found
        </h1>
      </div>
    );
  }

  return (
    <div>
      <div className="mb-6 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-gray-900">
          Evidence Details
        </h1>
        <Button variant="secondary" onClick={() => { /* Navigate back */ }}>
          Back to Cases
        </Button>
      </div>
      
      <div className="grid gap-6">
        <div className="lg:col-span-3">
          <Card>
            <h2 className="mb-4 text-xl font-semibold text-gray-900">
              Evidence Information
            </h2>
            <div className="space-y-4">
              <div className="text-sm">
                <span className="font-medium text-gray-600">Evidence ID:</span>
                <span className="ml-2 font-mono">{evidence.evidence_number}</span>
              </div>
              <div className="text-sm">
                <span className="font-medium text-gray-600">Original Filename:</span>
                <span className="ml-2">{evidence.original_filename}</span>
              </div>
              <div className="text-sm">
                <span className="font-medium text-gray-600">File Size:</span>
                <span className="ml-2">
                  {(evidence.file_size / 1024 / 1024).toFixed(2)} MB
                </span>
              </div>
              <div className="text-sm">
                <span className="font-medium text-gray-600">Dimensions:</span>
                <span className="ml-2">
                  {evidence.width} × {evidence.height} pixels
                </span>
              </div>
              <div className="text-sm">
                <span className="font-medium text-gray-600">Format:</span>
                <span className="ml-2">
                  {evidence.format} ({evidence.mime_type})
                </span>
              </div>
              <div className="text-sm">
                <span className="font-medium text-gray-600">Upload Time:</span>
                <span className="ml-2">{evidence.upload_timestamp}</span>
              </div>
              <div className="text-sm">
                <span className="font-medium text-gray-600">SHA-256:</span>
                <span className="ml-2 font-mono break-all block">
                  {evidence.sha256}
                </span>
              </div>
              <div className="text-sm">
                <span className="font-medium text-gray-600">MD5:</span>
                <span className="ml-2 font-mono break-all block">
                  {evidence.md5}
                </span>
              </div>
            </div>
          </Card>
        </div>
        
        <div className="lg:col-span-3">
          <Card>
            <h2 className="mb-4 text-xl font-semibold text-gray-900">
              File Integrity
            </h2>
            <div className="space-y-4">
              <div className="flex items-center">
                <div className="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                  <svg className="h-5 w-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <div className="ml-3">
                  <h3 className="font-medium text-gray-900">Hash Verification</h3>
                  <p className="text-sm text-gray-600">
                    Verifies that the evidence has not been altered since ingestion
                  </p>
                </div>
              </div>
              <Button 
                variant="primary" 
                className="w-full"
                onClick={() => { /* Trigger hash verification */ }}
              >
                Verify Integrity
              </Button>
              
              <div className="mt-4">
                <Badge 
                  variant="success" 
                  text="HASHES VERIFIED"
                />
                <p className="mt-2 text-sm text-gray-600">
                  The stored file matches the original hash values.
                </p>
              </div>
            </div>
          </Card>
        </div>
      </div>
      
      <div className="mt-6">
        <Button 
          variant="primary" 
          onClick={() => { /* Navigate to analysis */ }}
        >
          Start Forensic Analysis
        </Button>
      </div>
    </div>
  );
};

export default EvidenceDetail;
