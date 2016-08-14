from flask import Flask
from flask import jsonify
import json
from flask import Flask, session, redirect, url_for, escape, request



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/tem')
def hello_world21():
    return 'Hello, World!'



@app.route('/gift')
def user_gifts():
    return jsonify({'hello': "HHHH"})


@app.route('/api/<user>/gift')
def user_giftsww(user):
    return jsonify({'hello': "HHHH------"+ user})


@app.route('/api/gifts/lat/<lat>/lng/<lng>')
def user_giftsww555(lat, lng):
    return jsonify({'hello': "HHHH3333333", 'lng': lng, 'lat': lat})


@app.route('/api/new')
def get_gift():
	from firebase import firebase
	sam = firebase.FirebaseApplication('https://ssurppriseme.firebaseio.com/', None)
	result = sam.get('/box_items', None)
	
	return jsonify({'results': json.loads(json.dumps(result))})


@app.route('/api/new_gift', methods=['POST'])
def new_gift():
	if request.method == 'POST':
		from firebase import firebase
		sam = firebase.FirebaseApplication('https://ssurppriseme.firebaseio.com/', None)
		temp = request.data
		result = sam.post('/users', temp)
		return jsonify({'status': 'success' })	
    
if __name__=='__main__':
	app.run()    

