import React from 'react';

function Greeting({ name }) {
  return <h3>Hello, {name}</h3>;
}

function PropsDemo() {
  return <Greeting name="Amit" />;
}

export default PropsDemo;
