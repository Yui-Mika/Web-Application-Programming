function getWeather() {
    fetch('https://jsonplaceholder.typicode.com/users/1')
    .then(res => res.json())
    .then(data => {
        document.getElementById('weatherResult').textContent =
        'City: ' + data.address.city + ' (Fake Data Example)';
    });
}