from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/test"

mongo = PyMongo(app).db.test

@app.route('/products/', methods=['GET'])
def product_list():

    products = mongo.find()

    doc_list = json_util.dumps(products)
  
    return jsonify(doc_list)


#NOTE: use this db app.config['MONGO_URI'] = "mongodb://localhost:27017/test"
@app.route('/addproduct/', methods=['POST'])
def add():

    data = request.json

    mongo.insert_one(data)

    resp = jsonify("Added")

    resp.status_code = 200

    return resp
    
@app.route('/put/<int:id>', methods=['PUT'])
def put(id):
    data = request.get_json()
    name = data['name']

    mongo.db.products.update_one({'name': name})

    resp = jsonify("Added")

    resp.status_code = 200

    return resp
    
@app.route('/removeproduct/<int:id>', methods=['DELETE'])
def delete(id):
    
    mongo.delete_one({'_id': ObjectId(id)})

    resp = jsonify("DEleted")

    resp.status_code = 204

    return resp

if __name__ == '__main__':
    app.run(debug=True)