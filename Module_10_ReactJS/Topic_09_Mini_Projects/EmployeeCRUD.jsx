import React, { useState } from 'react';

function EmployeeCRUD() {
  const [employees, setEmployees] = useState([{ id: 1, name: 'Amit' }]);
  const [name, setName] = useState('');

  const addEmployee = () => {
    if (name) {
      setEmployees([...employees, { id: employees.length + 1, name }]);
      setName('');
    }
  };

  return (
    <div>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
      <button onClick={addEmployee}>Add</button>
      <ul>{employees.map((emp) => <li key={emp.id}>{emp.name}</li>)}</ul>
    </div>
  );
}

export default EmployeeCRUD;
