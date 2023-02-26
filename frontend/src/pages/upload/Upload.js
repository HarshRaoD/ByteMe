import React from 'react'
import FileUpload from '../../components/FileUpload/FileUpload'
import './Upload.css';

const Upload = () => {
  return (
    <div className='tools-body'>
        <h3 className='title'>Upload Research Paper</h3>
        <div className='file-upload' >
        <FileUpload />
        </div>       
    </div>
  )
}

export default Upload