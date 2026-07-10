import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function Home() { return <h2>Home</h2>; }
function About() { return <h2>About</h2>; }

function ReactRouter() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default ReactRouter;
