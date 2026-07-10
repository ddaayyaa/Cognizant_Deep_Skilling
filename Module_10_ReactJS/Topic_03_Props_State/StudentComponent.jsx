import React from 'react';

function StudentComponent({ student }) {
  return (
    <div>
      <h3>{student.name}</h3>
      <p>Roll: {student.roll}</p>
    </div>
  );
}

function StudentComponentWrapper() {
  const student = { name: 'Riya', roll: 12 };
  return <StudentComponent student={student} />;
}

export default StudentComponentWrapper;
