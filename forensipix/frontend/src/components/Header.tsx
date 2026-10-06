import React from 'react';
import { NavLink } from 'react-router-dom';
import { Menu, Logo, User, Settings as SettingsIcon } from 'lucide-react';

export const Header: React.FC = () => {
  return (
    <header className="bg-white shadow-md border-b">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
        <div className="flex items-center space-x-4">
          <NavLink to="/" className="flex items-center space-x-2 text-xl font-bold text-indigo-600">
            <Logo className="h-6 w-6" />
            <span>ForensiPix</span>
          </NavLink>
        </div>
        <div className="hidden md:flex items-center space-x-4">
          <NavLink to="/dashboard" className="text-gray-500 hover:text-gray-700 px-3 py-2 rounded-md hover:bg-gray-50">
            Dashboard
          </NavLink>
          <NavLink to="/cases" className="text-gray-500 hover:text-gray-700 px-3 py-2 rounded-md hover:bg-gray-50">
            Cases
          </NavLink>
          <NavLink to="/reports" className="text-gray-500 hover:text-gray-700 px-3 py-2 rounded-md hover:bg-gray-50">
            Reports
          </NavLink>
          <NavLink to="/settings" className="text-gray-500 hover:text-gray-700 px-3 py-2 rounded-md hover:bg-gray-50">
            Settings
          </NavLink>
        </div>
        <div className="flex items-center">
          <NavLink to="/settings" className="text-gray-500 hover:text-gray-700">
            <SettingsIcon className="h-5 w-5" />
          </NavLink>
        </div>
      </div>
    </header>
  );
};
