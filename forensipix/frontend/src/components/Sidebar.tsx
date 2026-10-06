import React from 'react';
import { NavLink } from 'react-router-dom';
import { 
  Layout, List, Clipboard, Folder, BarChart2, 
  FileText, Settings as SettingsIcon, LogOut
} from 'lucide-react';

export const Sidebar: React.FC = () => {
  return (
    <aside className="w-64 bg-white border-r shadow-sm">
      <div className="px-4 pt-5 pb-6">
        <NavLink to="/dashboard" className="flex flex-col items-start space-x-3 whitespace-nowrap">
          <Layout className="h-5 w-5 text-indigo-500" />
          <span className="font-medium text-gray-900">Dashboard</span>
        </NavLink>
      </div>
      <nav className="mt-6 space-y-2 px-3">
        <NavLink to="/cases" className="flex flex-col items-start space-x-3 whitespace-nowrap px-3 py-2 text-sm font-medium rounded-md">
          <List className="h-5 w-5 text-gray-400 group-hover:text-gray-900" />
          <span className="text-gray-700 group-hover:text-gray-900">Cases</span>
        </NavLink>
        <NavLink to="/evidence" className="flex flex-col items-start space-x-3 whitespace-nowrap px-3 py-2 text-sm font-medium rounded-md">
          <Clipboard className="h-5 w-5 text-gray-400 group-hover:text-gray-900" />
          <span className="text-gray-700 group-hover:text-gray-900">Evidence</span>
        </NavLink>
        <NavLink to="/analysis" className="flex flex-col items-start space-x-3 whitespace-nowrap px-3 py-2 text-sm font-medium rounded-md">
          <BarChart2 className="h-5 w-5 text-gray-400 group-hover:text-gray-900" />
          <span className="text-gray-700 group-hover:text-gray-900">Analysis</span>
        </NavLink>
        <NavLink to="/reports" className="flex flex-col items-start space-x-3 whitespace-nowrap px-3 py-2 text-sm font-medium rounded-md">
          <FileText className="h-5 w-5 text-gray-400 group-hover:text-gray-900" />
          <span className="text-gray-700 group-hover:text-gray-900">Reports</span>
        </NavLink>
      </nav>
      <div className="mt-auto px-4 pt-5 pb-6 border-t">
        <NavLink to="/settings" className="flex flex-col items-start space-x-3 whitespace-nowrap">
          <SettingsIcon className="h-5 w-5 text-indigo-500" />
          <span className="font-medium text-gray-900">Settings</span>
        </NavLink>
      </div>
    </aside>
  );
};
