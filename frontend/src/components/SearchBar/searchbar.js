import { useState } from 'react';
import { FaSearch } from 'react-icons/fa';

function SearchBar() {
  const [query, setQuery] = useState('');

  function handleSearch() {
    console.log(`Searching for: ${query}`);
    // Perform search functionality here
  }

  return (
    <div className="search-bar">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search"
      />
      <FaSearch onClick={handleSearch} />
    </div>
  );
}

export default SearchBar;