from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

# if a request POST is made on this url it runs the running function below
@app.route('/predict',methods=['POST']) 
def running():
    # receive the data
    req = request.get_json(force=True)  
    data = req['data']
    # create the response as a dict
    response = {'response': 'data received, ' + data + '!'} 
    # put the response in json and return
    return jsonify(response) 
