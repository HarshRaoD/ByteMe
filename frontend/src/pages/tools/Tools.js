import React from 'react'
import FileUpload from '../../components/FileUpload/FileUpload'
import Searchbar from '../../components/SearchBar/searchbar'
import './tools.css';

const Tools = () => {
  return (
    <div className='tools-body'>
        <h3 className='title'>Tools</h3>
        <FileUpload />
        <Searchbar />
    </div>
  )
}

export default Tools