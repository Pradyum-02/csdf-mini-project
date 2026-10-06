import React from 'react';

interface TableProps {
  children: React.ReactNode;
  className?: string;
}

const Table: React.FC<TableProps> = ({ children, className = '' }) => {
  return (
    <div className={`overflow-x-auto ${className}`}>
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          {children}
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {/* Table body would go here */}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
