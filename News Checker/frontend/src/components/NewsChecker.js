import React, { useState } from "react";
import axios from "axios";
import '../App.css';


const NewsChecker = () => {
    const [text, setText] = useState("");
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const handleCheck = async () => {
        setError(null);
        setResult(null);

        if (!text.trim()) {
            setError("Please enter some text to check.");
            return;
        }

        try {
            const response = await axios.post("http://127.0.0.1:50/predict", { text });
            setResult(response.data.prediction);
        } catch (error) {
            setError("Error checking news. Please try again.");
        }
    };

    return (
        <div style={{ textAlign: "center", marginTop: "20px" }}>
            <textarea
                rows="4"
                cols="50"
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Paste news text here..."
                style={{ padding: "10px", fontSize: "16px" }}
            />
            <br />
            <button onClick={handleCheck} style={{ padding: "10px 20px", fontSize: "16px" }}>
                Check
            </button>
            {result && <h3>Result: {result}</h3>}
            {error && <h3 style={{ color: "red" }}>{error}</h3>}
        </div>
    );
};

export default NewsChecker;
