from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homePage():
  return render_template("homepage.html")

# New Route

@app.route("/new")
def hello_new():
  return "Hello NEW Route!"

# you can also handle logic within your route function

@app.route("/math")
def handle_math():
  # equation = 15 *25
  return render_template("math.html")

@app.route("/fancy")
def html_world():
  return render_template("fancy.html")
