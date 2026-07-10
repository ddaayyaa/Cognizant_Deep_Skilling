import React from 'react';

function StudentPortal() {
  const student = { name: 'Maya', course: 'Java' };
  return (
    <div>
      <h1>Student Portal</h1>
      <p>Name: {student.name}</p>
      <p>Course: {student.course}</p>
    </div>
  );
}

export default StudentPortal;
