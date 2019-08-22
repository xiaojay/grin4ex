from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/deposit/<uid>/v2/foreign', methods=['POST'])
def index(uid):
    if request.json.get('method') == 'receive_tx':
        slate = request.json['params'][0]
        print(slate['id'])
        print(slate['amount'])

    url = 'http://127.0.0.1:3415/v2/foreign'
    r = requests.post(url, headers=request.headers, data=request.data)
    return r.text
