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
def new_g():
	from firebase import firebase
	sam = firebase.FirebaseApplication('https://ssurppriseme.firebaseio.com/', None)
	result = sam.get('/box_items', None)
	temp_3 = { 'location' : { 'lat': 65, 'lng': 61}, 'content': { 'type': 'message', 'value': '454544545' } }
	temp_2 = { 'location' : { 'lat': 85, 'lng': 50}, 'content': { 'type': 'message', 'value': 'Hello ADAS' } }
	temp_1 = { 'location' : { 'lat': 95, 'lng': 60}, 'content': { 'type': 'video', 'value': 'https://www.youtube.com/watch?v=Awadrec-tHk' } }

	print "NEW", result
	print type(result)
	#rr = sam.post('/box_items', temp)
	rr = sam.post('/box_items', temp_1)
	rr = sam.post('/box_items', temp_2)
	rr = sam.post('/box_items', temp_3)
	print "RRR", rr
	result = sam.get('/box_items', None)
	return jsonify({'results': json.loads(json.dumps(result))})
	#return 'Success'    
    
if __name__=='__main__':
	app.run()    

