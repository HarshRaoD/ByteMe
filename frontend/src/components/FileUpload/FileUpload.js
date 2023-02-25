import React, { useState } from 'react';
import './FileUpload.css';

function FileUpload() {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);

  function handleFileChange(e) {
    setFile(e.target.files[0]);
  }

  function handleDeleteClick() {
    setFile(null);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setUploading(true);
    const formData = new FormData();
    formData.append('file', file);
    try {
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) {
        throw new Error(response.statusText);
      }
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    } finally {
      setUploading(false);
    }
  }

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <label>
          Choose file:
          <input type="file" onChange={handleFileChange} />
        </label>
        {file && (
          <div className="selected-file">
            <p>{file.name}</p>
            <button type="delete-button" onClick={handleDeleteClick}>
              Delete
            </button>
          </div>
        )}
        <button type="submit" disabled={!file || uploading}>
          {uploading ? 'Uploading...' : 'Upload'}
        </button>
      </form>
    </div>
  );
}

export default FileUpload;
