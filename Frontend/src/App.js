import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [inputText, setInputText] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false); 
  const [error, setError] = useState("");

  const handleSummarize = async () => {
    if (!inputText.trim()) return;

    setLoading(true);    
    setSummary("");      
    setError("");

    try {
      const blob = new Blob([inputText], { type: "text/plain" });
      const file = new File([blob], "meeting.txt");

      const formData = new FormData();
      formData.append("file", file);

      const res = await axios.post("http://127.0.0.1:8000/summarize", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      if (res.data.error) {
        setError(res.data.error);
      } else {
        setSummary(res.data.summary);
      }
    } catch (err) {
      setError("Failed to connect to backend.");
      console.error(err);
    } finally {
      setLoading(false); 
    }
  };

  return (
    <div className="container">
      <h2>Lelouch : An AI Meeting Summarizer</h2>

      <textarea
        placeholder="Paste your meeting transcript here..."
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />

      <button onClick={handleSummarize} disabled={loading}>
        {loading ? "Summarizing..." : "Summarize"}
      </button>

      {loading && <p className="loading">##Please wait while we generate the summary...</p>}
      {error && <p className="error"> {error}</p>}

      {summary && (
        <>
          <h3>Summary</h3>
          <pre>{summary}</pre>
        </>
      )}
    </div>
  );
}

export default App;
