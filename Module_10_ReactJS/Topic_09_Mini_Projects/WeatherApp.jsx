import React, { useState, useEffect } from 'react';

function WeatherApp() {
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    setWeather({ temp: 25, condition: 'Sunny' });
  }, []);

  return (
    <div>
      <h1>Weather App</h1>
      {weather ? <p>{weather.condition}, {weather.temp}°C</p> : <p>Loading...</p>}
    </div>
  );
}

export default WeatherApp;
