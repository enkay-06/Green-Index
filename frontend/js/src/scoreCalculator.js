import { useEffect, useState } from "react";
import { calculateScore } from "./api";
import "./index.css";

export default function ScoreCalculator(){
    const [inputs, setInputs] = useState({});
    const [score, setScore] = useState(null);

    const handleChange = (e) => {
        const {name, value} = e.target;
        setInputs((prev)=>({...prev, [name]:isNaN(value) ? value:parseFloat(value)}));
        //copies all previous states, takes current state, checks if it's not a number (converts to float if is)
    };
    const handleSubmit = async()=>{
        const result = await calculateScore(inputs);
        setScore(result.score);
    }
  return (
    <div>
      <h2>Calculate Recyclability Score</h2>
      <input name="collection" placeholder="Collection (0-1)" onChange={handleChange} />
      <input name="sorting" placeholder="Sorting (0-1)" onChange={handleChange} />
      <input name="reprocessing" placeholder="Reprocessing (0-1)" onChange={handleChange} />
      <input name="material_health" placeholder="Material Health (0-1)" onChange={handleChange} />
      <input name="melting_point" placeholder="Melting Point (°C)" onChange={handleChange} />
      <input name="density" placeholder="Density (g/cm³)" onChange={handleChange} />
      <input name="toxicity" placeholder="Toxicity (Low/High)" onChange={handleChange} />
      <button onClick={handleSubmit}>Calculate</button>
      {score !== null && <p>Score: {score}</p>}
    </div>
  );
}