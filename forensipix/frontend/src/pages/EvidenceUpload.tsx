import React, { useState } from 'react';
import { Card } from '../components/Card';
import { Button } from '../components/Button';
import { DropzoneArea } from '../components/DropzoneArea';

const EvidenceUpload: React.FC = () => {
  const [uploading, setUploading] = useState(false);
  const [uploadComplete, setUploadComplete] = useState(false);
  const [evidenceId, setEvidenceId] = useState<string | null>(null);

  const handleUpload = async (file: File) => {
    setUploading(true);
    // In a real app, this would send the file to the backend API
    // For now, we'll simulate an upload
    try {
      // Simulate API call delay
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Mock successful upload
      setUploadComplete(true);
      setEvidenceId('EVD-0001');
    } catch (error) {
      console.error('Upload failed:', error);
      // In a real app, we'd show an error message
    } finally {
      setUploading(false);
    }
  };

  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold text-gray-900">
        Upload Evidence
      </h1>
      
      <Card>
        {!uploadComplete ? (
          <>
            <DropzoneArea onFileDrop={handleUpload} uploading={uploading} />
            {uploading && (
              <p className="mt-4 text-center text-gray-500">
                Uploading...
              </p>
            )}
          </>
        ) : (
          <>
            <div className="text-center py-8">
              <div className="mb-4">
                <svg className="mx-auto h-12 w-12 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <h2 className="mb-4 text-xl font-semibold text-gray-900">
                Evidence Successfully Uploaded
              </h2>
              <p className="mb-6 text-gray-600">
                Your evidence has been ingested and is ready for analysis.
              </p>
              <div className="space-y-4">
                <div className="text-left">
                  <h3 className="font-medium text-gray-900">Evidence ID:</h3>
                  <p className="pl-4 font-mono text-lg">{evidenceId}</p>
                </div>
                <div className="text-left">
                  <h3 className="font-medium text-gray-900">Integrity:</h3>
                  <p className="pl-4 px-2 py-1 bg-green-100 text-green-800 rounded">
                    VERIFIED
                  </p>
                </div>
              </div>
              <Button variant="primary" onClick={() => { /* Navigate to evidence detail */ }}>
                View Evidence Details
              </Button>
            </>
          </>
        )}
      </Card>
    </div>
  );
};

export default EvidenceUpload;
