#!flask/bin/python
from flask import Flask
from flask import request

from main2 import execute 

app = Flask(__name__) 

@app.route('/classify' , methods = ['POST'])

def index():
    data = request.json
    print(data["title"])
    
    title = data["title"]
    return execute(title)

if __name__ == '__main__':
    app.run(debug=True)