import React, { useState } from 'react';

const SearchBar = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  
  const handleInputChange = event => {
    setSearchTerm(event.target.value);
  };
  
  const handleSubmit = event => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('keyword', searchTerm);
    console.log(formData)
    fetch('http://localhost:9000/searchPapers/', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(data => {
        setSearchResults(data); // Update the state variable with search results
      })
      .catch(error => {
        console.error(error);
      });
  };
  
  
  return (
    <div className='searchbar-container'>
    <form onSubmit={handleSubmit}>
      <input type="text" value={searchTerm} onChange={handleInputChange} />
      <button type="submit">Search</button>
    </form>
    <br />
      {searchResults.map(result => (
        <li key={result.link}>
           
          <b>{result.title}</b>
          <br />
          <a href={result.link} target='_blank'>{result.link}</a> 
        </li>
      ))}
    
    </div>
  );
};

export default SearchBar;
