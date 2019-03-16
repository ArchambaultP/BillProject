import os
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

from app import create_app

app = create_app()
mongo = PyMongo(app)

@app.route('/star', methods=['GET'])
def get_all_stars():
    star = mongo.db.stars
    output = []
    for s in star.find():
        output.append({'name' : s['name'], 'distance' : s['distance']})
    return jsonify({'result' : output})

@app.route('/star/', methods=['GET'])
def get_one_star(name):
    star = mongo.db.stars
    s = star.find_one({'name' : name})
    if s:
        output = {'name' : s['name'], 'distance' : s['distance']}
    else:
        output = "No such name"
    return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']
    star_id = star.insert({'name': name, 'distance': distance})
    new_star = star.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance']}
    return jsonify({'result' : output})

@app.route('/register', methods=['POST'])
def add_user():
    user = mongo.db.users
    username = request.form.get('username')
    password = request.form.get('password')

    if user.find({'username' : {'$in': [username]}}).count() > 0:
        return jsonify({'result': 'username exists'}), 422
    
    user_id = user.insert({'username': username, 'password': password})
    new_user = user.find_one({'_id': user_id})
    output = {'username': new_user['username'], 'password' : new_user['password']}
    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3050, debug=True)
