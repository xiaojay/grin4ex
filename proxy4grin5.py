from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/v2/foreign', methods=['GET', 'POST'])
def index():
    if request.json.get('method') == 'receive_tx':
        slate = request.json['params'][0]
    url = 'http://127.0.0.1:3415/v2/foreign'
    resp = requests.post(url, headers=request.headers, data=request.data)
    if request.json.get('method') == 'receive_tx':
        slate = resp.json()
    return resp.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
