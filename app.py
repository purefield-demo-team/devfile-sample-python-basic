from flask import Flask
import os

app = Flask(__name__)
deployed_model_name = "fraud"
rest_url = "http://modelmesh-serving.redhat:8008"
infer_url = f"{rest_url}/v2/models/{deployed_model_name}/infer"

import requests
import pickle

def rest_request(data):
    json_data = {
        "inputs": [
            {
                "name": "dense_input",
                "shape": [1, 5],
                "datatype": "FP32",
                "data": data
            }
        ]
    }
    response = requests.post(infer_url, json=json_data)
    response_dict = response.json()
    return response_dict['outputs'][0]['data']

@app.route('/')
def hello():
    with open('artifact/scaler.pkl', 'rb') as handle:
        scaler = pickle.load(handle)


    # prediction parameter
    distance=200
    relative_price=10
    using_pin_number=1
    using_chip=1
    online_transaction=0
    data = [distance, relative_price, using_pin_number, using_chip, online_transaction]
    prediction = rest_request(scaler.transform([data]).tolist()[0])
    threshhold = 0.95
    fraudulent = 'fraud'

    if (prediction[0] <= threshhold):
        fraudulent = 'not fraud'

    return "Hello World!<br/>fraudulent: " + fraudulent + " <br/>prediction: "  + str( prediction[0] )

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
