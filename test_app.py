import os
import pytest
import json
import requests 
from app import app

url = 'http://127.0.0.1:5001/'

def test_api(app, client):

    # assert True
    name = "Chandra"

    function = 'call' 
    url_ = url+function 
    data = '{"name" :"'+str(name)+'"}'
    data = data.replace("'",'"')

    send_request = client.post(url_, data=data, follow_redirects=True)    

    assert send_request.status_code == 200
