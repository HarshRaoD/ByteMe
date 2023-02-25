import React, { useState } from 'react';

const SearchBar = () => {
  const [searchTerm, setSearchTerm] = useState('');
  
  const handleInputChange = event => {
    setSearchTerm(event.target.value);
  };
  
  const handleSubmit = event => {
    event.preventDefault();
    
    fetch(`https://example.com/api/search?q=${searchTerm}`)
      .then(response => response.json())
      .then(data => {
        // Do something with the API response data here
      })
      .catch(error => console.error(error));
  };
  
  return (
    <div className='searchbar-container'>
    <form onSubmit={handleSubmit}>
      <input type="text" value={searchTerm} onChange={handleInputChange} />
      <button type="submit">Search</button>
    </form>
    </div>
  );
};

export default SearchBar;
