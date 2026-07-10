import React, { useState } from 'react';

function LoginForm() {
  const [username, setUsername] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Logged in as ${username}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <button type="submit">Login</button>
    </form>
  );
}

export default LoginForm;
