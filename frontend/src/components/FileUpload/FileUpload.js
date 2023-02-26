import React, { useState } from 'react';
import './FileUpload.css';

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [oneLineSummary, setOneLineSummary] = useState('');
  const [wordCloud, setWordCloud] = useState('');

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && file.type !== "application/pdf") {
      alert("Please select a PDF file.");
      setSelectedFile(null);
    } else {
      setSelectedFile(file);
    }
  };

  const handleFileUpload = async () => {
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      // Upload file to endpoint localhost:9000/oneLineSummary/
      const oneLineSummaryResponse = await fetch("http://localhost:9000/oneLineSummary/", {
        method: "POST",
        body: formData,
      });
      const oneLineSummaryData = await oneLineSummaryResponse.json();
      setOneLineSummary(oneLineSummaryData.summary);

      // Upload file to endpoint localhost:9000/getWordCloud/
      const wordCloudResponse = await fetch("http://localhost:9000/getWordCloud/", {
        method: "POST",
        body: formData,
      });
      const wordCloudData = await wordCloudResponse.json();
      setWordCloud(wordCloudData.image);

      // Handle success logic here
    } catch (error) {
      setOneLineSummary("Error in generating the summary");
      setWordCloud("Error in generating the word cloud")
    }
  };

  const handleFileDelete = () => {
    setSelectedFile(null);
    setOneLineSummary('');
    setWordCloud('');
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
      {oneLineSummary && (
        <div>
          <h2>One-line summary:</h2>
          <p>{oneLineSummary}</p>
        </div>
      )}
      {wordCloud && (
        <div>
          <h2>Word cloud:</h2>
          <img src={`data:image/png;base64,${wordCloud}`} alt="Word cloud" />
        </div>
      )}
    </div>
  );
};

export default FileUpload;
