import React, { useEffect, useState } from 'react';
import axios from 'axios';

function CarbonChargeTime() {
  const [time, setTime] = useState([]);

  useEffect(() => {
    const apiUrl = "http://127.0.0.1:5000/api/mincarboncharge/4"
    axios.get(apiUrl)
      .then((response) => {
        setTime(response.data.time)
      })
    }, []);

  const returnTime = Date(time).toLocaleString('en-US', { timeZone: 'America/New_York' })
  return (
    <div>
      <p>API Data: {time}</p>
    </div>
  );
}

export default CarbonChargeTime;