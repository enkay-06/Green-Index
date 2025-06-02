import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { createRoot } from "react-dom/client";
import "./index.css";


const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);
//Render the App component into the HTML element with ID of root