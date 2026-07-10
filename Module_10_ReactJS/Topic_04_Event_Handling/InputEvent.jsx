import React, { useState } from 'react';

function InputEvent() {
  const [text, setText] = useState('');

  return (
    <div>
      <input value={text} onChange={(event) => setText(event.target.value)} />
      <p>You typed: {text}</p>
    </div>
  );
}

export default InputEvent;
