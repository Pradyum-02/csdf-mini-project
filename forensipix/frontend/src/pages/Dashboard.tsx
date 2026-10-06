import React, { useState, useEffect } from 'react';
import { Card } from '../components/Card';
import { Stat } from '../components/Stat';

const Dashboard: React.FC = () => {
  const [stats, setStats] = useState({
    cases: 0,
    evidence: 0,
    analyses: 0,
    flagged: 0
  });

  useEffect(() => {
    // In a real app, this would fetch data from the API
    // For now, we'll use mock data
    setStats({
      cases: 12,
      evidence: 48,
      analyses: 43,
      flagged: 9
    });
  }, []);

  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold text-gray-900">
        Dashboard
      </h1>
      
      <div className="grid gap-6 mb-8">
        <div className="grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
          <Stat title="Cases" value={stats.cases} icon="Users" color="blue" />
          <Stat title="Evidence Items" value={stats.evidence} icon="FileText" color="green" />
          <Stat title="Analyses" value={stats.analyses} icon="Activity" color="purple" />
          <Stat title="Flagged Evidence" value={stats.flagged} icon="AlertTriangle" color="red" />
        </div>
      </div>
      
      <div className="grid gap-6">
        <div className="col-span-1 lg:col-span-3">
          <Card>
            <h2 className="mb-4 text-xl font-semibold text-gray-900">
              Recent Cases
            </h2>
            <div className="space-y-4">
              {/* Mock case items */}
              <div className="p-4 bg-gray-50 rounded-lg border">
                <div className="flex justify-between items-start">
                  <div>
                    <h3 className="font-medium text-gray-900">Social Media Image Investigation</h3>
                    <p className="text-sm text-gray-500">CASE-2026-0012</p>
                  </div>
                  <span className="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full">
                    Active
                  </span>
                </div>
                <p className="mt-2 text-sm text-gray-600">
                  Analysis of a potentially manipulated image from social media.
                </p>
              </div>
              
              <div className="p-4 bg-gray-50 rounded-lg border">
                <div className="flex justify-between items-start">
                  <div>
                    <h3 className="font-medium text-gray-900">Document Authentication Review</h3>
                    <p className="text-sm text-gray-500">CASE-2026-0011</p>
                  </div>
                  <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">
                    Completed
                  </span>
                </div>
                <p className="mt-2 text-sm text-gray-600">
                  Forensic analysis of disputed documents.
                </p>
              </div>
            </div>
          </Card>
        </div>
        
        <div className="lg:col-span-3">
          <Card>
            <h2 className="mb-4 text-xl font-semibold text-gray-900">
              Recent Activity
            </h2>
            <div className="space-y-4">
              {/* Mock activity items */}
              <div className="p-4 bg-gray-50 rounded-lg border">
                <div className="flex justify-between items-start">
                  <div className="flex items-center space-x-3">
                    <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                      {/* Upload icon */}
                      <svg className="h-5 w-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 16l5-5m0 0l5 5m-5-5v12m-3-4h18" />
                      </svg>
                    </div>
                    <div>
                      <h3 className="font-medium text-gray-900">New evidence uploaded</h3>
                      <p className="text-sm text-gray-500">EVD-0047 added to CASE-2026-0012</p>
                    </div>
                  </div>
                  <span className="text-sm text-gray-400">2 min ago</span>
                </div>
              </div>
              
              <div className="p-4 bg-gray-50 rounded-lg border">
                <div className="flex justify-between items-start">
                  <div className="flex items-center space-x-3">
                    <div className="w-8 h-8 bg-purple-100 rounded-full flex items-center justify-center">
                      {/* Analysis icon */}
                      <svg className="h-5 w-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                      </svg>
                    </div>
                    <div>
                      <h3 className="font-medium text-gray-900">Analysis completed</h3>
                      <p className="text-sm text-gray-500">ELA and noise analysis finished for EVD-0045</p>
                    </div>
                  </div>
                  <span className="text-sm text-gray-400">15 min ago</span>
                </div>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
