import json
import pytest

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_weather_existing_city(client):
    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['temperature'] == 14
    assert data['weather'] == 'Cloudy'

def test_get_weather_nonexistent_city(client):
    response = client.get('/weather/Chicago')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error'] == 'City not found'

def test_add_weather(client):
    data = {
        'city': 'Chicago',
        'temperature': 18,
        'weather': 'Cloudy'
    }
    response = client.post('/weather', json=data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Weather data added successfully'

def test_update_weather(client):
    data = {
        'temperature': 30,
        'weather': 'Sunny'
    }
    response = client.put('/weather/San Francisco', json=data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Weather data updated successfully'
    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['temperature'] == 30
    assert data['weather'] == 'Sunny'

def test_delete_weather(client):
    response = client.delete('/weather/Seattle')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Weather data deleted successfully'
    response = client.get('/weather/Seattle')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error'] == 'City not found'