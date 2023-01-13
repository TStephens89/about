import sys
import pytest
import sqlite3
import requests
import os
import app
from flask import Flask
import app
import psycopg2
import tempfile

url = os.getenv("DATABASE_URL")

@pytest.fixture
def setup_database():
    conn = psycopg2.connect(url)
    cursor = conn.cursor()
    cursor.execute('''
	    CREATE TABLE IF NOT EXISTS enclosures
        (id SERIAL PRIMARY KEY, name TEXT)''')
    sample_data = [
        (10, "Grass"),
        (20, "Fire"),
    ]
    cursor.executemany('INSERT INTO enclosures VALUES(%s, %s)', sample_data)
    
    cursor.execute('''
	    CREATE TABLE IF NOT EXISTS pokemans
        (enclosure_id INTEGER, pokeman TEXT, quantity REAL, pokeman_id INTEGER)''')
    sample_data2 = [
        (1, "Onion Turtle", 32, 1),
        (2, "Punchy Rock", 12, 2),
    ]
    cursor.executemany('INSERT INTO pokemans VALUES(%s, %s, %s, %s)', sample_data2)
    yield conn, cursor


@pytest.fixture
def client():
    application = app.create_app({"TESTING": True})
    with application.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200 

def test_get_route(client):
    response = client.get('/api/enclosure/1')
    print("this is the response: " + str(response.json))
    assert str(response.json) == "{'name': 'Grass'}"



        
def test_helloworld_page(client):

    resp = client.get('/')
    print(resp) 

def test_connection(setup_database):
    conn, cursor = setup_database
    cursor.execute('SELECT * FROM enclosures')
    cursor.execute('SELECT * FROM pokemans')
    result = cursor.fetchmany(2)
    print("the expected output for mock data is 2")
    assert len(list(result)) == 2
    # print("test start expected output is: 2\nActual: " + result)

def test_data(setup_database):
  conn, cursor = setup_database
  cursor.execute('SELECT name FROM enclosures WHERE id = 1')
  result = cursor.fetchone()
  print("the result expected result: ('Grass',)\n Actual: " + str(result))
  assert str(result) == "('Grass',)"

def test_file_exists():
  print("Testing for existence of report file")
  assert os.path.exists('./report.html')
  