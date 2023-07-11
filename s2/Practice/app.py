from flask import Flask, jsonify, request
import json

data = [{"id": 1, "dish": "samosa", "price": 20}, {"id": 2, "dish": "jalebi", "price": 40}]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def read():
    with open("data.json","r") as file:
        data = json.load(file)

    response = jsonify({"data":data})   
    response.status_code = 200
    return response

@app.route("/",methods=['POST'])
def create():
    dish_data = request.json
    # print(dish_data)
    with open("data.json","r") as file:
        current_data =  json.load(file)
    
    current_data.append(dish_data)

    with open("data.json","w") as file:
        json.dump(current_data,file)

    response = jsonify({'message': 'New Dish added successfully'})
    response.status_code = 200
    return response

@app.route("/<int:index>",methods=["PUT"])
def update(index):
    dish_data = request.json

    with open("data.json","r") as file:
        current_data = json.load(file)
    
    for i in range(0,len(current_data)):
        if current_data[i]["id"] == int(index):
          print(current_data[i])
          current_data[i] = dish_data

    with open("data.json","w") as file:
        json.dump(current_data,file) 

    response = jsonify({'data': "data hasbeen updated successfully"})
    response.status_code = 200
    return response   

if __name__ == '__main__':
    app.run(port=10000)