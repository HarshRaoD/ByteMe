import React from 'react'
import FileUpload from '../../components/FileUpload/FileUpload'
import Searchbar from '../../components/SearchBar/searchbar'

const home = () => {
  return (
    <div>
        <h1>Home Page</h1>
        <Searchbar />
        <FileUpload />
    </div>
  )
}

export default home