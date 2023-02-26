import React from 'react';
import NavigationBar from './components/Navbar/Navbar.js';
import Home from './pages/home/Home.js';
import Tools from './pages/upload/Upload.js';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";
import Search from './pages/search/Search.js';

function App() {
  return (
    <div className='App'>
      <Router>
        <NavigationBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/home" element={<Home />} />
          <Route path="/upload" element={<Tools />} />
          <Route path="/search" element={<Search />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;