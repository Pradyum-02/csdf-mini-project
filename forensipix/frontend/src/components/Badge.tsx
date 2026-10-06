import React from 'react';

interface BadgeProps {
  variant?: 'default' | 'primary' | 'secondary' | 'success' | 'warning' | 'error';
  text: string;
  className?: string;
}

const Badge: React.FC<BadgeProps> = ({ 
  variant = 'default', 
  text, 
  className = '' 
}) => {
  const variantClasses = {
    default: 'bg-gray-200 text-gray-800',
    primary: 'bg-indigo-600 text-white',
    secondary: 'bg-gray-300 text-gray-900',
    success: 'bg-green-500 text-white',
    warning: 'bg-yellow-500 text-black',
    error: 'bg-red-500 text-white'
  };
  
  const classes = `inline-flex items-center px-3 py-1 rounded-full text-xs font-medium ${variantClasses[variant]} ${className}`.trim();
  
  return <span className={classes}>{text}</span>;
};

export default Badge;
