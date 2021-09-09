import requests
import json
import argparse
from pathlib import Path
import curlify

	
def curl_request(url,method,headers,payloads):
    # construct the curl command from request
    command = "curl -v -H {headers} {data} -X {method} {uri}"
    data = "" 
    if payloads:
        payload_list = ['"{0}":"{1}"'.format(k,v) for k,v in payloads.items()]
        data = " -d '{" + ", ".join(payload_list) + "}'"
    header_list = ['"{0}: {1}"'.format(k, v) for k, v in headers.items()]
    header = " -H ".join(header_list)
    print(command.format(method=method, headers=header, data=data, uri=url))



if __name__ == '__main__':

	# local url
	# url = 'http://192.168.17.228:5001/'
	url = 'http://localhost:5001/'

	method = 'POST'
	headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

	# default vars
	name = "Chandra"

	function = 'call' 
	url_ = url+function 
	data = '{"name" :"'+str(name)+'"}'
	data = data.replace("'",'"')
	data_json = json.loads(data)

	print(url_,	data)

	send_request = requests.post(url_, data, headers=headers, verify=False)

	print(curlify.to_curl(send_request.request))

	if send_request.status_code == 200:

		print(send_request.json())
	else:
		print('There is an error occurs')

	#

	method = 'GET'
	headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

	# default vars
	name = "Chandra"

	function = ''
	url_ = url+function
	data = '{"name" :"'+str(name)+'"}'
	data = data.replace("'",'"')
	data_json = json.loads(data)

	print(url_,	data)

	send_request = requests.get(url_, headers=headers, verify=False)

	print(curlify.to_curl(send_request.request))

	if send_request.status_code == 200:

		# print(send_request.json())
		print(send_request)
	else:
		print('There is an error occurs')
