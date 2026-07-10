import React from 'react';

function Child() {
  return <p>I am a child component.</p>;
}

function NestedComponent() {
  return (
    <div>
      <h2>Nested Component</h2>
      <Child />
    </div>
  );
}

export default NestedComponent;
