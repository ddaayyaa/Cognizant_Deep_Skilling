import React, { useState, useEffect } from 'react';

function AsyncAwaitDemo() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('https://jsonplaceholder.typicode.com/users');
      const result = await response.json();
      setUsers(result.slice(0, 3));
    }
    fetchData();
  }, []);

  return (
    <div>
      <h1>Users</h1>
      <ul>{users.map((user) => <li key={user.id}>{user.name}</li>)}</ul>
    </div>
  );
}

export default AsyncAwaitDemo;
