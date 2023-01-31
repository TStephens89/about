import sys
import pytest
import sqlite3
import requests
import os
import app
from flask import Flask
import tempfile
from bson import json_util
from bson.objectid import ObjectId
import webbrowser
import urllib
import re
import json
import codecs


url = 'http://127.0.0.5000'

@pytest.fixture
def client():
    application = app.create_app({"TESTING": True})
    with application.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    
def test_get_status(client):
    response = client.get('/part/63d183e2b3cf215b1291dd57')
    assert response.status_code == 200

def test_get_part(client):
    response = client.get('/part/63d183e2b3cf215b1291dd57')
    print("this is the string: " + str(response.data))
    info = str(response.data)
    assert codecs.decode(response.data) == '{"_id": {"$oid": "63d183e2b3cf215b1291dd57"}, "PartName": "Silicon", "SKU": "5165", "Qty": "25", "Weight": "10", "Cost($)": "15", "Dimensions": "10x10", "Expiration": "N/A"}'

def test_post_route(client):
    response = client.post('/part', json={"PartName": " not more paper", "SKU": "5165", "Qty": "25", "Weight": "10", "Cost($)": "15", "Dimensions": "10x10", "Expiration": "N/A"}
    )
    assert response.status_code == 200

def test_delete_route(client):
    response = client.delete('/part/63d43c02441c922f1c27a5fd')
    assert response.status_code == 200
  
def test_file_exists():
  print("Testing for existence of report file")
  assert os.path.exists('./report.html')  
    