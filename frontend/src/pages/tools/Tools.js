import React from 'react'
import FileUpload from '../../components/FileUpload/FileUpload'
import Searchbar from '../../components/SearchBar/searchbar'
import './tools.css';

const Tools = () => {
  return (
    <div className='tools-body'>
        <h3 className='title'>Tools</h3>
        <div className='file-upload' >
        <FileUpload />
        </div>

        <div className='search-bar'>
        <Searchbar />
        </div>
       
    </div>
  )
}

export default Tools