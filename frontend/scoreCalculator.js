import React, { use, useState } from "react";
import { calculateScore } from "./api";

export default function scoreCalculator(){
    const [inputs, setInputs] = useState({});
    const [score, setScore] = useState(null);

    const handleChange = (e) => {
        const {name, value} = e.target;
        setInputs((prev)=>({...prev, [name]:isNaN(value) ? value:parseFloat(value)}));
        //copies all previous states, takes current state, checks if it's not a number (converts to float if is)
    };
    }

    const handleSubmit = async()=>{}