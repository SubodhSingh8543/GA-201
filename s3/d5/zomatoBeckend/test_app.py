import pytest
import json
from app import app, collection, orderCollection

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

# Test Case: Retrieve All Data
def test_get_data(client):
    # Add some test data to the 'dish' collection
    test_dishes = [
        {'dish_name': 'Dish 1', 'price': 10.99, 'availability': True},
        {'dish_name': 'Dish 2', 'price': 15.99, 'availability': False}
    ]
    collection.insert_many(test_dishes)

    # Make a GET request to '/data'
    response = client.get('/data')

    # Assert the response
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == len(test_dishes)
    assert data[0]['dish_name'] == test_dishes[0]['dish_name']

    # Clean up: Remove test data
    collection.delete_many({})

# Test Case: Add New Data
def test_add_data(client):
    # Prepare a JSON payload with dish details
    new_dish = {'dish_name': 'New Dish', 'price': 19.99, 'availability': True}

    # Make a POST request to '/data' with the payload
    response = client.post('/data', data=json.dumps(new_dish), content_type='application/json')

    # Assert the response
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'id' in data

    # Clean up: Remove the inserted dish
    collection.delete_many({'_id': data['id']})

# Test Case: Update Existing Data
def test_update_data(client):
    # Add a test dish to the 'dish' collection
    test_dish = {'dish_name': 'Test Dish', 'price': 12.99, 'availability': True}
    result = collection.insert_one(test_dish)
    test_dish_id = str(result.inserted_id)

    # Prepare a JSON payload with the updated dish details
    updated_dish = {'dish_name': 'Updated Dish', 'price': 15.99, 'availability': False}

    # Make a PUT request to '/data/<id>' with the payload and the ID of the test dish
    response = client.put(f'/data/{test_dish_id}', data=json.dumps(updated_dish), content_type='application/json')

    # Assert the response
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Document updated successfully'

    # Clean up: Remove the test dish
    collection.delete_many({'_id': test_dish_id})

# Test Case: Delete Existing Data
def test_delete_data(client):
    # Add a test dish to the 'dish' collection
    test_dish = {'dish_name': 'Test Dish', 'price': 12.99, 'availability': True}
    result = collection.insert_one(test_dish)
    test_dish_id = str(result.inserted_id)

    # Make a DELETE request to '/data/<id>' with the ID of the test dish
    response = client.delete(f'/data/{test_dish_id}')

    # Assert the response
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Document deleted successfully'

    # Clean up: Remove the test dish
    collection.delete_many({'_id': test_dish_id})

# Test Case: Add Order
def test_order_data(client):
    # Prepare a JSON payload with order details
    new_order = {'dish_name': 'Dish 1', 'price': 10.99, 'username': 'user123'}

    # Make a POST request to '/order' with the payload
    response = client.post('/order', data=json.dumps(new_order), content_type='application/json')

    # Assert the response
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'id' in data

    # Clean up: Remove the inserted order
    orderCollection.delete_many({'_id': data['id']})

# Test Case: Retrieve All Orders
def test_get_order(client):
    # Add some test orders to the 'order' collection
    test_orders = [
        {'dish_name': 'Dish 1', 'price': 10.99, 'username': 'user1'},
        {'dish_name': 'Dish 2', 'price': 15.99, 'username': 'user2'}
    ]
    orderCollection.insert_many(test_orders)

    # Make a GET request to '/order'
    response = client.get('/order')

    # Assert the response
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == len(test_orders)
    assert data[0]['username'] == test_orders[0]['username']

    # Clean up: Remove test orders
    orderCollection.delete_many({})