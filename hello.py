""" Minimal flask app"""

from flask import flask

#Make the applicaiton
app = Flash(__name__)

#Make the route
@app.route("/")

#Now define a function
def hello:
  return "Hello World"
  
