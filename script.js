document.getElementById('searchBtn').addEventListener('click', function() {
  let city = document.getElementById('cityInput').value;
  fetchWeather(city);
});

function fetchWeather(city) {
  const apiKey = '358abdb51f2648d4aaa51249232812'; 
  const url = `https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${city}&aqi=no`;

  fetch(url)
  .then(response => {
      if (!response.ok) {
          throw new Error(`Ошибка: ${response.status}`);
      }
      return response.json();
  })
  .then(data => {
      displayWeather(data);
  })
  .catch(error => {
      console.error('Ошибка при получении данных погоды:', error);
  });
}

function displayWeather(data) {
  const { location, current } = data;
  const { name } = location;
  const { temp_c, condition, humidity, wind_kph } = current;

  document.getElementById('weatherResult').innerHTML = `
      <h2>Погода в ${name}</h2>
      <img src="${condition.icon}" alt="Weather icon">
      <p>Температура: ${temp_c}°C</p>
      <p>Описание: ${condition.text}</p>
      <p>Влажность: ${humidity}%</p>
      <p>Скорость ветра: ${wind_kph} км/ч</p>
  `;
}