import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("idle" | "uploading" | "success" | "error");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  }

  const handleUpload = async () => {
    // Alerts if there is no file uploaded
    if (!file) return alert("Please upload a PDF file."); 
    setStatus("Uploading")

    const formData = new FormData();
    formData.append("resume", file);

    try {
      await axios.post('http://127.0.0.1:5000/api/parse-resume', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setStatus("Success");
      console.log(status);
      
    } catch (error) {
      setStatus("Error");
      alert("File upload failed. Check console for error details.");
    }
  };

  return (
    <div>
      <h1>AI Resume Analyzer</h1>
      <input type="file" accept='application/pdf' onChange={handleFileChange} />
      {file && status != "Uploading" && <button onClick={handleUpload}>Upload Resume</button>}
    </div>
  );
}

export default App
