import React, { useState, useEffect } from 'react';
import { Card } from '../components/Card';
import { Button } from '../components/Button';
import { Tabs } from '../components/Tabs';
import { ForensicSummary } from '../components/ForensicSummary';

const EvidenceAnalysis: React.FC = () => {
  const [analysisData, setAnalysisData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('overview');

  useEffect(() => {
    // In a real app, this would fetch data from the API
    // For now, we'll use mock data
    setTimeout(() => {
      setAnalysisData({
        metadata: {
          editing_software_detected: ["Adobe Photoshop"],
          metadata_complete: true,
          basic_info: {
            width: 1920,
            height: 1080,
            format: "JPEG",
            mode: "RGB"
          },
          exif_data: {
            Make: "Canon",
            Model: "EOS R5",
            Software: "Adobe Photoshop 2020 (Windows)"
          },
          gps_info: {
            latitude: 40.7128,
            longitude: -74.0060
          }
        },
        integrity: {
          sha256_verified: true,
          md5_verified: true
        },
        ela: {
          has_significant_anomalies: true,
          max_intensity: 45,
          interpretation: "ELA highlights regions with different compression characteristics. These differences can be caused by editing, but may also occur naturally."
        },
        noise: {
          has_significant_anomalies: false,
          noise_variance: 12.5,
          interpretation: "Noise patterns appear consistent across the image."
        },
        copy_move: {
          has_significant_matches: true,
          matches_found: 8,
          interpretation: "Found 8 potential copy-move matches. This may indicate duplicated or moved regions in the image."
        },
        provenance: {
          provenance_found: false,
          interpretation: "No C2PA/provenance metadata detected. This does NOT mean the image is manipulated."
        },
        ai: {
          available: false,
          reason: "AI model not configured"
        }
      });
      setLoading(false);
    }, 1500);
  }, []);

  if (loading) {
    return (
      <div className="p-8">
        <h1 className="mb-6 text-2xl font-bold text-gray-900">
          Forensic Analysis
        </h1>
        <div className="text-center py-12">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500"></div>
        </div>
      </div>
    );
  }

  if (!analysisData) {
    return (
      <div className="p-8">
        <h1 className="mb-6 text-2xl font-bold text-gray-900">
          Analysis Data Not Available
        </h1>
      </div>
    );
  }

  return (
    <div>
      <div className="mb-6 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-gray-900">
          Forensic Analysis
        </h1>
        <Button variant="secondary" onClick={() => { /* Navigate back */ }}>
          Back to Evidence
        </Button>
      </div>
      
      <div className="space-y-6">
        <ForensicSummary 
          analysis={analysisData} 
        />
        
        <Tabs 
          activeTab={activeTab}
          onTabChange={setActiveTab}
        >
          {/* Tab contents would go here */}
        </Tabs>
      </div>
    </div>
  );
};

export default EvidenceAnalysis;
