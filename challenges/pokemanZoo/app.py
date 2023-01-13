from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import psycopg2


load_dotenv()

app = Flask(__name__)

url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

CREATE_ENCLOSURES_TABLE = (
    "CREATE TABLE IF NOT EXISTS enclosures (id SERIAL PRIMARY KEY, name TEXT);"
)

CREATE_POKEMAN_TABLE = (
    "CREATE TABLE IF NOT EXISTS pokemans (enclosure_id INTEGER, pokeman TEXT, quantity REAL, pokeman_id INTEGER, FOREIGN KEY(enclosure_id) REFERENCES enclosures(id) ON DELETE CASCADE);"
)

INSERT_ENCLOSURE_RETURN_ID = "INSERT INTO enclosures (name) VALUES (%s) RETURNING id;"
INSERT_POKEMAN = (
    "INSERT INTO pokemans (enclosure_id, pokeman, quantity, pokeman_id) VALUES (%s, %s, %s, %s);"
)

ENCLOSURE_SELECT = """SELECT name FROM enclosures WHERE id = (%s)"""
POKEMAN_SELECT = """SELECT name FROM pokemans WHERE id = (%s)"""

@app.get("/")
def home():
  return "ZooDex"

# @app.get("/api/enclosure/<int:enclosure_id>")
# def get_enclosure_all(enclosure_id):
#   with connection:
#     with connection.cursor() as cursor:
#       cursor.execute(ENCLOSURE_SELECT, (enclosure_id,))
#       name = cursor.fetchone()[0]
    
#   return {"name": name, }, 201

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/')
    def index():
        return 'Testing'
    @app.get("/api/enclosure/<int:enclosure_id>")
    def get_enclosure_all(enclosure_id):
      with connection:
        with connection.cursor() as cursor:
          cursor.execute(ENCLOSURE_SELECT, (enclosure_id,))
          name = cursor.fetchone()[0]
    
      return {"name": name, }, 201
    

    return app

@app.post("/api/enclosure")
def create_enclosure():
  data = request.get_json()
  name = data["name"]


  with connection:
  
    with connection.cursor() as cursor:
      cursor.execute(CREATE_ENCLOSURES_TABLE)
      cursor.execute(INSERT_ENCLOSURE_RETURN_ID, (name,))
      enclosure_id = cursor.fetchone()[0]
  return {"id": enclosure_id, "message": f"Enclosure {name} created."}, 201

@app.post("/api/Pokeman")
def add_pokeman():
  data = request.get_json()
  pokeman = data["pokeman"]
  quantity = data["quantity"]
  enclosure_id = data["enclosure"]
  pokeman_id = data["pokeman_id"]
  
  with connection:
    with connection.cursor() as cursor:
      cursor.execute(CREATE_POKEMAN_TABLE)
      cursor.execute(INSERT_POKEMAN, (enclosure_id, pokeman, quantity, pokeman_id))
  return {"message": "Pokeman added."}, 201


