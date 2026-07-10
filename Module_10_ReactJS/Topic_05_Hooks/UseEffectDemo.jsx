import React, { useState, useEffect } from 'react';

function UseEffectDemo() {
  const [time, setTime] = useState(new Date().toLocaleTimeString());

  useEffect(() => {
    const interval = setInterval(() => setTime(new Date().toLocaleTimeString()), 1000);
    return () => clearInterval(interval);
  }, []);

  return <div>Current time: {time}</div>;
}

export default UseEffectDemo;
