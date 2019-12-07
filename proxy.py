from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/deposit/<uid>/v2/foreign', methods=['GET', 'POST'])
def index(uid):
    #put uid to db and associate with this tx.
    print('Request headers: {}'.format(request.headers))
    print('Request data: {}'.format(request.data))

    if request.json.get('method') == 'receive_tx':
        slate = request.json['params'][0]
        print(slate['id'])
        print(slate['amount'])
        #put id\amount to db 
    url = 'http://127.0.0.1:3415/v2/foreign'
    resp = requests.post(url, headers=request.headers, data=request.data)
    if request.json.get('method') == 'receive_tx':
        print(resp.json())
        slate = resp.json()
        #uxtos (inputs/outpus) for this tx
        inputs = slate['result']['Ok']['tx']['body']['inputs']
        outputs = slate['result']['Ok']['tx']['body']['outputs']
        #put the slate/inputs/outputs to db
    
    print('Response: {}'.format(resp.text))
    return resp.text

if __name__ == '__main__':
    app.run(host='0.0.0.0')
