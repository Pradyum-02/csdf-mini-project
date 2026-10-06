import React, { useState } from 'react';

interface DropzoneAreaProps {
  onFileDrop: (file: File) => Promise<void>;
  uploading?: boolean;
  className?: string;
}

const DropzoneArea: React.FC<DropzoneAreaProps> = ({ 
  onFileDrop, 
  uploading = false,
  className = ''
}) => {
  const [dragActive, setDragActive] = useState(false);

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setDragActive(true);
  };

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault();
    setDragActive(false);
  };

  const handleDrop = async (e: React.DragEvent) => {
    e.preventDefault();
    setDragActive(false);
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      await onFileDrop(files[0]);
    }
  };

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      await onFileDrop(file);
    }
    // Reset input to allow same file to be selected again
    e.target.value = '';
  };

  const dragClasses = dragActive 
    ? 'border-2 border-dashed border-indigo-500 bg-indigo-50' 
    : 'border-2 border-dashed border-gray-300 bg-gray-50 hover:bg-gray-100';

  return (
    <div className={`p-12 text-center rounded-lg border ${dragClasses} ${className}`}
         onDragOver={handleDragOver}
         onDragLeave={handleDragLeave}
         onDrop={handleDrop}
    >
      <input
        type="file"
        accept="image/*"
        className="hidden"
        onChange={handleFileChange}
      />
      
      {!uploading ? (
        <>
          <div className="mb-6">
            <svg className="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M7 16l4-4m0 0l4-4m-4 4H14m-5 4v6a2 2 0 002 2h6a2 2 0 002-2v-6M13 8h6M6 8h6" />
            </svg>
          </div>
          <h3 className="mb-4 text-xl font-semibold text-gray-900">
            Drop evidence here
          </h3>
          <p className="mb-4 text-gray-600">
            Or click to select a file
          </p>
          <div className="space-y-2 text-sm text-gray-500">
            <div>Supported: JPEG / PNG / TIFF / WEBP</div>
            <div>Maximum size: 50 MB</div>
          </div>
          <Button 
            variant="secondary" 
            onClick={() => document.querySelector('input[type="file"]')?.click()}
          >
            Select File
          </Button>
        </>
      ) : (
        <>
          <div className="mb-4">
            <svg className="mx-auto h-12 w-12 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 7v10c0 2 2 4 4 4h6c2 0 4-2 4-4V7m2-2h3a2 2 0 012 2v3a2 2 0 01-2 2H9a2 2 0 01-2-2v-3a2 2 0 012-2h3z" />
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 9h.01" />
            </svg>
          </div>
          <p className="text-lg font-medium text-gray-900">
            Processing upload...
          </p>
        </>
      )}
    </div>
  );
};

export default DropzoneArea;
