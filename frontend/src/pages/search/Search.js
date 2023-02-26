import React from 'react'
import SearchBar from '../../components/SearchBar/searchbar'
import './search.css'

const Search = () => {
  return (
    <div className='tools-body'>
        <h3 className='title'>Search for research papers</h3>
        <div className='search-bar'>
        <SearchBar />
        </div>
    </div>
  )
}

export default Search