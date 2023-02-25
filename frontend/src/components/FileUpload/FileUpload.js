import React, { useState } from 'react';
import './FileUpload.css';
import { FaFileAlt, FaTrashAlt } from 'react-icons/fa';

function FileUpload() {
  const [file, setFile] = useState(null);

  function handleFileChange(event) {
    setFile(event.target.files[0]);
  }

  function handleDelete() {
    setFile(null);
  }

  return (
    <div className="file-upload-container">
      <h2>Upload a File</h2>
      <div className="file-container">
        <div className="file-input-container">
          {file ? (
            <div className="selected-file">
              <span className="selected-file-name">{file.name}</span>
              <button className="selected-file-delete-button" onClick={handleDelete}>
                <FaTrashAlt /> Delete
              </button>
            </div>
          ) : (
            <label htmlFor="file-input" className="choose-file-button">
              <FaFileAlt /> Choose File
            </label>
          )}
          <input
            type="file"
            id="file-input"
            onChange={handleFileChange}
            accept=".jpg,.jpeg,.png,.pdf,.doc,.docx"
          />
        </div>
      </div>
    </div>
  );
}

export default FileUpload;