import pytest
import flask
from app import app

from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>hello from python and git<h1/>'

if __name__=='__main__':
    app.run(debug=True)



def test_request():
  TestResponse=app.test_client().get('/')
  response_status=TestResponse.status_code
  #print(response_status)
  response_data=TestResponse.data
  #print(response_data)
  assert response_status==200 ,'invalid response'
  assert response_data==b'<h1>hello from python and git<h1/>'