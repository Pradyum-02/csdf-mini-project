import React, { useState } from 'react';
import { Card } from '../components/Card';
import { Button } from '../components/Button';
import { Table } from '../components/Table';

const Cases: React.FC = () => {
  const [cases, setCases] = useState([
    {
      id: 1,
      case_number: 'CASE-2026-0001',
      title: 'Social Media Image Investigation',
      description: 'Analysis of a potentially manipulated image.',
      investigator: 'Alex Johnson',
      status: 'Active',
      evidence_count: 5
    },
    {
      id: 2,
      case_number: 'CASE-2026-0002',
      title: 'Document Authentication Review',
      description: 'Forensic analysis of disputed documents.',
      investigator: 'Maria Garcia',
      status: 'Completed',
      evidence_count: 3
    }
  ]);

  return (
    <div>
      <div className="mb-6 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-gray-900">
          Cases
        </h1>
        <Button variant="primary" onClick={() => { /* Navigate to create case */ }}>
          New Case
        </Button>
      </div>
      
      <Card>
        {cases.length > 0 ? (
          <Table>
            <thead>
              <tr>
                <th className="text-left px-4 py-3">Case Number</th>
                <th className="text-left px-4 py-3">Title</th>
                <th className="text-left px-4 py-3">Investigator</th>
                <th className="text-left px-4 py-3">Status</th>
                <th className="text-left px-4 py-3">Evidence</th>
                <th className="text-left px-4 py-3">Actions</th>
              </tr>
            </thead>
            <tbody>
              {cases.map((caseItem) => (
                <tr key={caseItem.id} className="border-t hover:bg-gray-50">
                  <td className="px-4 py-3">{caseItem.case_number}</td>
                  <td className="px-4 py-3">{caseItem.title}</td>
                  <td className="px-4 py-3">{caseItem.investigator}</td>
                  <td className="px-4 py-3">
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                      caseItem.status === 'Active' 
                        ? 'bg-blue-100 text-blue-800' 
                        : 'bg-green-100 text-green-800'
                    }`}>
                      {caseItem.status}
                    </span>
                  </td>
                  <td className="px-4 py-3">{caseItem.evidence_count}</td>
                  <td className="px-4 py-3 space-x-2">
                    <Button variant="secondary" size="sm" onClick={() => { /* View case */ }}>
                      View
                    </Button>
                    <Button variant="outline" size="sm" onClick={() => { /* Edit case */ }}>
                      Edit
                    </Button>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
        ) : (
          <p className="text-center py-8 text-gray-500">
            No cases found. Create your first case to get started.
          </p>
        )}
      </Card>
    </div>
  );
};

export default Cases;
