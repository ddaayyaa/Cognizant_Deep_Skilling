import React, { useState } from 'react';

function MouseEvent() {
  const [status, setStatus] = useState('Mouse out');

  return (
    <div>
      <button onMouseEnter={() => setStatus('Mouse over')} onMouseLeave={() => setStatus('Mouse out')}>
        Hover me
      </button>
      <p>{status}</p>
    </div>
  );
}

export default MouseEvent;
