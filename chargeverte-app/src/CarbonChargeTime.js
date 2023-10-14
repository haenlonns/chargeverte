import React, { useEffect, useState } from 'react';
import axios from 'axios';

function CarbonChargeTime() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/mincarboncharge/5')
    .then((response) => {
      setData(response.data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }, []);

  return (
    <div>
      <h1>React App Listening to Flask API</h1>
      <p>API Data: {JSON.stringify(data)}</p>
    </div>
  );
}

export default CarbonChargeTime;