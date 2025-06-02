import React from "react";
import MaterialComparison from "./materialComparison";
import ScoreCalculator from "./scoreCalculator";

function App() {
  return (
    <div>
      <h1>Recyclability Score Predictor</h1>
      <MaterialComparison />
      <ScoreCalculator />
    </div>
  );
}

export default App;