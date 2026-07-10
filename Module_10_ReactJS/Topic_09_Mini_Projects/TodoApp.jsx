import React, { useState } from 'react';

function TodoApp() {
  const [task, setTask] = useState('');
  const [todos, setTodos] = useState([]);

  const addTask = () => {
    if (task) {
      setTodos([...todos, task]);
      setTask('');
    }
  };

  return (
    <div>
      <input value={task} onChange={(e) => setTask(e.target.value)} placeholder="New task" />
      <button onClick={addTask}>Add</button>
      <ul>{todos.map((item, index) => <li key={index}>{item}</li>)}</ul>
    </div>
  );
}

export default TodoApp;
