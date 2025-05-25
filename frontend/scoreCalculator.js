import React, { use, useState } from "react";
import { calculateScore } from "./api";

export default function scoreCalculator(){
    const [inputs, setInputs] = useState({});
    const [score, setScore] = useState(null);

    const