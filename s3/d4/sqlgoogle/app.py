from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# MongoDB Atlas connection configuration
client = MongoClient('mongodb+srv://subodhsingh8543:u6UEfmEX4wjePt4t@cluster0.qfutgem.mongodb.net/mydatabase?retryWrites=true&w=majority')
db = client['mydatabase']
collection = db['dish']

# Route for retrieving data
@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find())

    # Convert data to a list of dictionaries
    result = []
    for document in data:
        result.append({
            'id': str(document['_id']),
            'dish_name': document['dish_name'],
            'price': document['price'],
            'availability': document['availability']
            # Add more fields as needed
        })

    return jsonify(result)

# Route for adding data
@app.route('/data', methods=['POST'])
def add_data():
    data = request.get_json()
    document = data

    result = collection.insert_one(document)

    return jsonify({'id': str(result.inserted_id)})

# Route for updating data
@app.route('/data/<id>', methods=['PUT'])
def update_data(id):
    data = request.get_json()
    update_fields = {}

    for key, value in data.items():
        update_fields[key] = value

    result = collection.update_one({'_id': ObjectId(id)}, {'$set': update_fields})

    if result.modified_count > 0:
        return jsonify({'message': 'Document updated successfully'})
    else:
        return jsonify({'message': 'No document found with the provided ID'})


if __name__ == '__main__':
    app.run(port=10000)
