#!/usr/bin/python3


from flask import Flask

app = Flask(__name__)

# SUGGESTION 1: create another endpoint, copy lines 8-10 and make a new one 
@app.route("Mohamed")
def hello_world():
   return "Hello World"
   # SUGGESTION 2: instead of returning a string like on line 10, return a dictionary. It will become JSON in your browser!
   # SUGGESTION 3: try creating some data on a topic of your choice and display it as JSON

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
 
