import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [name, setName] = useState("");
  const [response, setResponse] = useState(null);

  const handleSubmit = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/api/parse-resume", {
        name: name
      });
      setResponse(res.data.message);
    } catch (err) {
      console.error(err);
      setResponse("Error occurred");
    }
  };

  return (
    <div>
      <h1>AI Resume Analyzer</h1>
      <input 
        type="text"
        placeholder='Enter name'
        value={name}
        onChange={(e) => setName(e.target.value)} 
      />
      <button onClick = {handleSubmit}>Submit</button>
      {response && <p>{response}</p>}
    </div>
  );
}

export default App
