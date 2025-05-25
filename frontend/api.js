export async function fetchMaterials() {
  const response = await fetch("http://localhost:5000/materials")
    return response.json();
}
export async function fetchMaterialDetails(name) {
  const response = await fetch(`http://localhost:5000/material/${name}`);
  return response.json();
}

export async function calculateScore(materialProps) {
  const response = await fetch("http://localhost:5000/score", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(materialProps),
  });
  return response.json();
}
