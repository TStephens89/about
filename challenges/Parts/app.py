from flask import Flask, request
from pymongo import MongoClient
from mongopass import mongopass
from bson import json_util
from bson.objectid import ObjectId
import json


app = Flask(__name__)

client = MongoClient(mongopass)
db = client["Parts"]
collection = db["part names"]

@app.route("/")
def index():
  data = []
  for d in collection.find():
    data.append(d)
    
  return json_util.dumps(data, indent=4, default=json_util.default), 200

@app.route("/part/<part_id>")
def get_part(part_id):
  part = collection.find_one({"_id": ObjectId(part_id)})
  if part:
    return json_util.dumps(part), 200
  else:
    return json_util.dumps({"error": "part not found."}), 404

  
@app.route("/part", methods=["POST"])
def create_part():
  part = request.get_json()
  result = collection.insert_one(part)
  return json_util.dumps({"id": str(result.inserted_id)})

@app.route("/part/<part_id>", methods=["PUT"])
def update_part(part_id):
  part = request.get_json()
  result = collection.update_one({"_id": ObjectId(part_id)}, {"$set": part})
  if result.matched_count > 0:
    return json_util.dumps({"status": "success"})
  else:
    return json_util.dumps({"error": "part not found"}), 404
  
@app.route("/part/<part_id>", methods=["DELETE"])
def delete_part(part_id):
  result = collection.delete_one({"_id": ObjectId(part_id)})
  if result.deleted_count > 0:
    return json_util.dumps({"status": "success"})
  else:
    return json_util.dumps({"error": "part not found"}), 404

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/')
    def index():
        return 'Testing'
    
    @app.route("/part/<part_id>")
    def get_part(part_id):
      part = collection.find_one({"_id": ObjectId(part_id)})
      if part:
        return json_util.dumps(part), 200
      else:
        return json_util.dumps({"error": "part not found."}), 404
    
    @app.route("/part", methods=["POST"])
    def create_part():
      part = request.get_json()
      result = collection.mongo.db.insert_one(part)
      return json_util.dumps({"id": str(result.inserted_id)})
    @app.route("/part/<part_id>", methods=["DELETE"])
    def delete_part(part_id):
      result = collection.delete_one({"_id": ObjectId(part_id)})
      if result.deleted_count > 0:
        return json_util.dumps({"status": "success"})
      else:
        return json_util.dumps({"error": "part not found"}), 404

    return app
  


if __name__ == '__main__':
  app.run(DEBUG=true)