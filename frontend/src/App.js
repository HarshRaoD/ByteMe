import React from 'react';
import NavigationBar from './components/Navbar/Navbar.js';
import Home from './pages/home/home.js';
import Tools from './pages/tools/Tools.js';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";

function App() {
  return (
    <div className='App'>
      <Router>
        <NavigationBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/home" element={<Home />} />
          <Route path="/tools" element={<Tools />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;