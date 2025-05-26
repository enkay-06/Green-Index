import React, { useEffect, useState } from "react";
import { fetchMaterials, fetchMaterialDetails } from "./api";

export default function MaterialComparison() {
  const [materials, setMaterials] = useState([]);
  const [details, setDetails] = useState({});

  useEffect(() => {
    fetchMaterials().then(setMaterials);
  }, []);
  // fetch materials when array is empty

  const handleClick = async (name) => {
    const data = await fetchMaterialDetails(name);
    setDetails(data);
  };

  return (
    <div>
      <h2>Compare Materials</h2>
      {materials.map((name) => (
        <button key={name} onClick={() => handleClick(name)}>{name}</button>
      ))}
      {/*creates a button for each material*/}
      {details && (
        <pre>{JSON.stringify(details, null, 2)}</pre>
      )}
        {/* displays the details of the selected material */}
    </div>
  );
}