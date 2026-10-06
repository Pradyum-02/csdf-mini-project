import React from 'react';

interface TabsProps {
  activeTab: string;
  onTabChange: (tab: string) => void;
  className?: string;
  children: React.ReactNode;
}

const Tabs: React.FC<TabsProps> = ({ 
  activeTab, 
  onTabChange, 
  className = '',
  children
}) => {
  // Extract direct children as tabs
  const tabs = React.Children.toArray(children).filter(
    child => React.isValidElement(child) && child.type.displayName === 'Tab'
  );
  
  return (
    <div className={className}>
      <div className="border-b border-gray-200 mb-6">
        <div className="flex">
          {tabs.map((tab, index) => {
            const tabProps = tab.props;
            const isActive = activeTab === tabProps.eventKey;
            
            return (
              <button
                key={index}
                onClick={() => onTabChange(tabProps.eventKey)}
                className={`${isActive 
                  ? 'border-b-2 border-indigo-500 text-indigo-600 px-4 py-3' 
                  : 'text-gray-500 hover:text-gray-700 px-4 py-3'}`
                }
              >
                {tabProps.title}
              </button>
            );
          })}
        </div>
      </div>
      <div className="mt-4">
        {/* Active tab content would be shown here */}
        {tabs.map(tab => {
          if (activeTab === tab.props.eventKey) {
            return <div key={tab.props.eventKey} className="mt-4">{tab.props.children}</div>;
          }
          return null;
        })}
      </div>
    </div>
  );
};

interface TabProps {
  title: string;
  eventKey: string;
  children: React.ReactNode;
}

const Tab: React.FC<TabProps> = ({ title, eventKey, children }) => {
  return (
    <div 
      style={{ display: 'none' }} 
      data-title={title} 
      data-event-key={eventKey}
    >
      {children}
    </div>
  );
};

Tab.displayName = 'Tab';

export { Tabs, Tab };
