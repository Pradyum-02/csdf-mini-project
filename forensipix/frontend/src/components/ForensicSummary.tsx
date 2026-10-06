import React from 'react';
import { Card } from './Card';
import { Badge } from './Badge';

interface ForensicSummaryProps {
  analysis: {
    metadata: {
      editing_software_detected: string[];
      metadata_complete: boolean;
    };
    integrity: {
      sha256_verified: boolean;
      md5_verified: boolean;
    };
    ela: {
      has_significant_anomalies: boolean;
      max_intensity: number;
      interpretation: string;
    };
    noise: {
      has_significant_anomalies: boolean;
      noise_variance: number;
      interpretation: string;
    };
    copy_move: {
      has_significant_matches: boolean;
      matches_found: number;
      interpretation: string;
    };
    provenance: {
      provenance_found: boolean;
      interpretation: string;
    };
    ai: {
      available: boolean;
      reason?: string;
    };
  };
}

const ForensicSummary: React.FC<ForensicSummaryProps> = ({ analysis }) => {
  // Calculate risk score (simplified version)
  let score = 0;
  
  // Metadata anomalies
  if (analysis.metadata.editing_software_detected.length > 0) {
    score += Math.min(analysis.metadata.editing_software_detected.length * 5, 15);
  }
  if (!analysis.metadata.metadata_complete) {
    score += 5;
  }
  
  // ELA
  if (analysis.ela.has_significant_anomalies) {
    score += Math.min(Math.floor(analysis.ela.max_intensity / 10), 20);
  }
  
  // Noise
  if (analysis.noise.has_significant_anomalies) {
    score += 15;
  }
  
  // Copy-move
  if (analysis.copy_move.has_significant_matches) {
    score += Math.min(analysis.copy_move.matches_found, 20);
  }
  
  // Provenance (inverted - no provenance is slightly concerning)
  if (!analysis.provenance.provenance_found) {
    score += 10;
  }
  
  // AI
  if (analysis.ai.available) {
    score += Math.floor((analysis.ai.confidence || 0) * 20);
  }
  
  // Cap score at 100
  score = Math.min(score, 100);
  
  // Determine risk level
  let riskLevel: string;
  let riskColor: string;
  
  if (score <= 24) {
    riskLevel = "LOW";
    riskColor = "green";
  } else if (score <= 49) {
    riskLevel = "MODERATE";
    riskColor = "yellow";
  } else if (score <= 74) {
    riskLevel = "HIGH";
    riskColor = "orange";
  } else {
    riskLevel = "CRITICAL";
    riskColor = "red";
  }
  
  return (
    <Card>
      <h2 className="mb-4 text-xl font-semibold text-gray-900">
        Forensic Summary
      </h2>
      
      <div className="mb-6">
        <div className="flex items-center">
          <div className={`w-10 h-10 rounded-full bg-${riskColor}-100 flex items-center justify-center mr-3`}>
            <span className={`text-${riskColor}-800 font-bold`}>{score}</span>
          </div>
          <div>
            <h3 className="font-medium text-gray-900">
              Forensic Risk Score
            </h3>
            <p className="text-sm text-gray-600">
              {riskLevel} Risk ({score}/100)
            </p>
          </div>
        </div>
        
        <div className="mt-4 p-4 bg-gray-50 rounded-lg">
          <p className="text-sm text-gray-600">
            This score is an investigative prioritization indicator,
            not a probability that the image is fake.
          </p>
        </div>
      </div>
      
      <div className="space-y-4">
        <div>
          <h3 className="font-medium text-gray-900 mb-2">
            Integrity
          </h3>
          <Badge variant={analysis.integrity.sha256_verified && analysis.integrity.md5_verified ? "success" : "error"}>
            {analysis.integrity.sha256_verified && analysis.integrity.md5_verified ? "VERIFIED" : "HASH MISMATCH"}
          </Badge>
        </div>
        
        <div>
          <h3 className="font-medium text-gray-900 mb-2">
            Metadata
          </h3>
          <Badge 
            variant={analysis.metadata.editing_software_detected.length > 0 ? "warning" : "success"}
          >
            {analysis.metadata.editing_software_detected.length > 0 
              ? `EDITING SOFTWARE DETECTED (${analysis.metadata.editing_software_detected.join(", ")})`
              : "NO EDITING SOFTWARE DETECTED"
            }
          </Badge>
        </div>
        
        <div>
          <h3 className="font-medium text-gray-900 mb-2">
            ELA Analysis
          </h3>
          <Badge variant={analysis.ela.has_significant_anomalies ? "warning" : "success"}>
            {analysis.ela.has_significant_anomalies ? "POTENTIAL ANOMALIES" : "NO SIGNIFICANT ANOMALIES"}
          </Badge>
        </div>
        
        <div>
          <h3 className="font-medium text-gray-900 mb-2">
            Noise Analysis
          </h3>
          <Badge variant={analysis.noise.has_significant_anomalies ? "warning" : "success"}>
            {analysis.noise.has_significant_anomalies ? "ABNORMAL PATTERNS" : "NO SIGNIFICANT ANOMALIES"}
          </Badge>
        </div>
        
        <div>
          <h3 className="font-medium text-gray-900 mb-2">
            Copy-Move Analysis
          </h3>
          <Badge variant={analysis.copy_move.has_significant_matches ? "warning" : "success"}>
            {analysis.copy_move.has_significant_matches ? `POTENTIAL MATCHES (${analysis.copy_move.matches_found})` : "NO SIGNIFICANT MATCHES"}
          </Badge>
        </div>
        
        <div>
          <h3 className="font-medium text-gray-900 mb-2">
            Provenance
          </h3>
          <Badge variant={analysis.provenance.provenance_found ? "success" : "error"}>
            {analysis.provenance.provenance_found ? "DETECTED" : "NOT AVAILABLE"}
          </Badge>
        </div>
        
        <div>
          <h3 className="font-medium text-gray-900 mb-2">
            AI-Assisted Analysis
          </h3>
          <Badge variant={analysis.ai.available ? "success" : "error"}>
            {analysis.ai.available ? "CONFIGURED" : "NOT CONFIGURED"}
          </Badge>
        </div>
      </div>
    </div>
  );
};

export default ForensicSummary;
