from flask import Flask, jsonify, request
import json

app = Flask(__name__)

data = [
    { "id":1, "username": "sksingh", "caption": "nice" },
    { "id":2, "username": "chunnu", "caption": "nice" },
    { "id":3, "username": "munnu", "caption": "nice" }
]

@app.route("/",methods=["GET"])
def read():
    responce = jsonify({"data":data})
    responce.status_code = 200
    return responce

@app.route("/",methods=["POST"])
def create():
    new_post = request.json

    data.append(new_post)

    responce = jsonify({"msg":"post has been created"})
    responce.status_code = 200
    return responce

@app.route("/<int:index>",methods=["DELETE"])
def delete(index):
    global data 
    newData = []

    for i in data:
        if i["id"] == int(index):
            continue
        else:
            newData.append(i)
            data = newData
    responce = jsonify({"msg":data})
    responce.status_code = 200
    return responce

if __name__ == "__main__":
    app.run(port=11000)