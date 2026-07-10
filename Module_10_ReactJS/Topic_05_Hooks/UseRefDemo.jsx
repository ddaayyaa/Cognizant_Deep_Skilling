import React, { useRef } from 'react';

function UseRefDemo() {
  const inputRef = useRef(null);

  const focusInput = () => inputRef.current && inputRef.current.focus();

  return (
    <div>
      <input ref={inputRef} placeholder="Focus me" />
      <button onClick={focusInput}>Focus input</button>
    </div>
  );
}

export default UseRefDemo;
