import React from 'react';

interface StatProps {
  title: string;
  value: number | string;
  icon: keyof typeof LucideIcons;
  color?: 'blue' | 'green' | 'purple' | 'red' | 'gray';
}

// Simple icon mapping - in a real app, we'd import from lucide-react properly
const LucideIcons = {
  Users: 'users',
  FileText: 'file-text',
  Activity: 'activity',
  AlertTriangle: 'alert-triangle'
};

const Stat: React.FC<StatProps> = ({ title, value, icon, color = 'gray' }) => {
  const colorClasses = {
    blue: 'border-blue-500 bg-blue-50 text-blue-900',
    green: 'border-green-500 bg-green-50 text-green-900',
    purple: 'border-purple-500 bg-purple-50 text-purple-900',
    red: 'border-red-500 bg-red-50 text-red-900',
    gray: 'border-gray-300 bg-gray-50 text-gray-900'
  };

  return (
    <div className={`p-6 rounded-lg border ${colorClasses[color] || colorClasses.gray}`}>
      <div className="flex items-center mb-3">
        <div className="w-8 h-8 flex items-center justify-center">
          {/* Simplified icon representation */}
          <span className="text-xs">{icon}</span>
        </div>
        <h3 className="ml-3 text-sm font-medium text-gray-500">
          {title}
        </h3>
      </div>
      <p className="text-3xl font-bold">
        {value}
      </p>
    </div>
  );
};

export default Stat;
