import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AxiosDemo() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get('https://jsonplaceholder.typicode.com/posts')
      .then((response) => setPosts(response.data.slice(0, 3)));
  }, []);

  return (
    <div>
      <h1>Axios Posts</h1>
      <ul>{posts.map((post) => <li key={post.id}>{post.title}</li>)}</ul>
    </div>
  );
}

export default AxiosDemo;
