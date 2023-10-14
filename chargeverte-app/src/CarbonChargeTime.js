import React, { useEffect, useState } from 'react';

function CarbonChargeTime() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/mincarboncharge/5') // Replace with your Flask API URL
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div>
      <h1>React App Listening to Flask API</h1>
      <p>API Data: {JSON.stringify(data)}</p>
    </div>
  );
}

export default CarbonChargeTime;