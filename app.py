import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import json


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('list', type=list)


@app.route('/')
def hello():

	return jsonify('Hello there!!')

@app.route('/call', methods=['POST'])
def call():

	ABC = parser.parse_args()
	data_decoded = request.data.decode("utf-8") 

	#convert to json
	data_json = json.loads(data_decoded)
	print(data_json)


	if 'name' in data_json:
		name = data_json['name']
	else:
		name is None


	if isinstance(name,str) and name is not None:

		output = "Hi, "+name+'!! Have a good day!!'

	else:

		output = "Whoever you are, I wish you a good day!! "

	output = json.dumps(output)

	return jsonify(output)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5001))
	app.run(host='0.0.0.0', port = port, debug=True)

	# local
	# app.run(host='127.0.0.1', port = port, debug=True)
	