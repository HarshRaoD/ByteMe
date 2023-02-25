import React, { useState } from 'react';
import './FileUpload.css';

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleFileUpload = () => {
    // Handle file upload logic here
  };

  const handleFileDelete = () => {
    setSelectedFile(null);
  };

  return (
    <div className="file-upload-container">
      {selectedFile ? (
        <div className="selected-file-container">
          <p>{selectedFile.name}</p>
          <button onClick={handleFileDelete}>Delete</button>
        </div>
      ) : (
        <div className="file-select-container">
          <input type="file" onChange={handleFileChange} />
        </div>
      )}
      <button disabled={!selectedFile} onClick={handleFileUpload}>
            Upload
          </button>
    </div>
  );
};

export default FileUpload;
