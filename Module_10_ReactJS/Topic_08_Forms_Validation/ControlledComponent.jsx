import React, { useState } from 'react';

function ControlledComponent() {
  const [value, setValue] = useState('');
  return (
    <div>
      <input value={value} onChange={(e) => setValue(e.target.value)} />
      <p>Current value: {value}</p>
    </div>
  );
}

export default ControlledComponent;
