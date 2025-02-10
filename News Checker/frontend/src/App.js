import './App.css';
import React from "react";
import NewsChecker from "./components/NewsChecker";

function App() {
  return (
      <div>
          <h1 style={{ textAlign: "center", marginTop: "20px" }}>News Checker System</h1>
          <NewsChecker />
      </div>
  );
}

export default App;