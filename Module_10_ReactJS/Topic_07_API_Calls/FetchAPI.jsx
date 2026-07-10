import React, { useState, useEffect } from 'react';

function FetchAPI() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then((response) => response.json())
      .then((result) => setData(result.slice(0, 3)));
  }, []);

  return (
    <div>
      <h1>Posts</h1>
      <ul>{data.map((item) => <li key={item.id}>{item.title}</li>)}</ul>
    </div>
  );
}

export default FetchAPI;
