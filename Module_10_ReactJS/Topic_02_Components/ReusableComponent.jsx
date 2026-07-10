import React from 'react';

function Button({ label }) {
  return <button>{label}</button>;
}

function ReusableComponent() {
  return (
    <div>
      <Button label="Save" />
      <Button label="Cancel" />
    </div>
  );
}

export default ReusableComponent;
