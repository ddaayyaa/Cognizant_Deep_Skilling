import React from 'react';

function ButtonClick() {
  const handleClick = () => alert('Button clicked!');

  return <button onClick={handleClick}>Click Me</button>;
}

export default ButtonClick;
