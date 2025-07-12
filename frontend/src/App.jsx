import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  }

  const handleUpload = async () => {
    // Alerts if there is no file uploaded
    if (!file) return alert("Please upload a PDF file."); 

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const response = axios.post('http://127.0.0.1:5000/api/parse-resume', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setText(response.data.text);
    } catch (err) {
      console.error(err);
      alert('Upload Failed.');
    }
  };
}

export default App
