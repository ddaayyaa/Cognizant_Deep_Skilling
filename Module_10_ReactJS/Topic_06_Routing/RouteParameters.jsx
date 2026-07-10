import React from 'react';
import { useParams } from 'react-router-dom';

function RouteParameters() {
  const { id } = useParams();
  return <div>Route parameter: {id}</div>;
}

export default RouteParameters;
