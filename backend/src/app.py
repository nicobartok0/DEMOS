from flask import Flask, request
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonreactdb'
mongo = PyMongo(app)

db = mongo.db.users

@app.route('/users', methods=['POST'])
def createUser():
    id = db.insert({
        "name": request.json["name"],
        "email": request.json["email"],
        "password": request.json["password"]
    })
    print(str(ObjectId(id)))
    return 'recibido'

@app.route('/users', methods=['GET'])
def getUsers():
    return 'recibido'

@app.route('/user/', methods=['GET'])
def getUser():
    return 'recibido'

@app.route('/users/<id>', methods=['GET'])
def deleteUser():
    return 'recibido'

@app.route('/users/<id>', methods=['PUT'])
def updateUser():
    return 'recibido'

if __name__ == '__main__':
    app.run(debug=True)
