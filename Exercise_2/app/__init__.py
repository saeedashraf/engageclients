#!flask/bin/python
from flask import Flask
from flask import request

from main_fun import execute 

app = Flask(__name__) 

@app.route('/classify' , methods = ['POST'])

def index():
    data = request.json
    print(data["user_id"])
    print(data["os"])
    print(data["browser"])
    print(data["plan"])
    print(data["page"])
    
    user_id = data["user_id"]
    os = data["os"]
    browser = data["browser"]
    plan = data["plan"]
    page = data["page"]
    
    return execute(user_id, os, browser, plan, page)

if __name__ == '__main__':
    app.run(debug=True)