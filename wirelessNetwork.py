from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

import os
app = Flask(__name__)

distance = 0


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/refresh_data')
def refresh_data():
    data = {'distance': str(distance)}
    return jsonify(data)

@app.route('/update_data')
def update_data():
    dis = request.args.get('distance')
    global distance
    distance = dis
    return str(distance)
@app.route('/takeoff')
def takeoff():
    os.system("echo takeoff success")
    return "0"
@app.route('/land')
def land():
    os.system("echo land success?")
    return "0"
app.run(host='0.0.0.0', port=1001)