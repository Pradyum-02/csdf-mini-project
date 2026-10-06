import React from 'react';

interface CardProps {
  children: React.ReactNode;
  className?: string;
}

const Card: React.FC<CardProps> = ({ children, className = '' }) => {
  return (
    <div className={`bg-white rounded-lg shadow-md border ${className}`}>
      <div className="p-6">
        {children}
      </div>
    </div>
  );
};

export default Card;
