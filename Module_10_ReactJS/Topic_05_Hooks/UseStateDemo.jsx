import React, { useState } from 'react';

function UseStateDemo() {
  const [value, setValue] = useState('Hello');

  return (
    <div>
      <p>{value}</p>
      <button onClick={() => setValue('React Hooks')}>Change</button>
    </div>
  );
}

export default UseStateDemo;
