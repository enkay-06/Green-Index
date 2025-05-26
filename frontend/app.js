import React from "react";
import materialComparison from "./materialComparison";
import scoreCalculator from "./scoreCalculator";

function App() {
  return (
    <div>
      <h1>Recyclability Score Predictor</h1>
      <scoreCalculator />
      <saterialComparison />
    </div>
  );
}

export default App;