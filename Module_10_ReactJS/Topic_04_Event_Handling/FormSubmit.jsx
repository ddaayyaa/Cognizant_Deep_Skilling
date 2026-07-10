import React, { useState } from 'react';

function FormSubmit() {
  const [name, setName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Submitted: ${name}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
      <button type="submit">Submit</button>
    </form>
  );
}

export default FormSubmit;
