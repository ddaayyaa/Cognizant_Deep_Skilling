import React, { useState, useEffect } from 'react';

function JSONPlaceholder() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/todos')
      .then((response) => response.json())
      .then((data) => setTodos(data.slice(0, 3)));
  }, []);

  return (
    <div>
      <h1>Todos</h1>
      <ul>{todos.map((todo) => <li key={todo.id}>{todo.title}</li>)}</ul>
    </div>
  );
}

export default JSONPlaceholder;
