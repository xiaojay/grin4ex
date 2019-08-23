import requests, json, sys
from requests.auth import HTTPBasicAuth

url = 'http://localhost:3420/v2/owner'
api_sercet = '<your api_sercet file location>'
tx_id = sys.argv[1]

headers = {
    'Content-Type': 'application/json'
}
auth = HTTPBasicAuth('grin', open(api_sercet).read().strip())
payload = {
    'jsonrpc': '2.0',
    'id': '1',
    'method': 'retrieve_txs',
    'params': [True, None, tx_id],
}
client = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
result = client.json()
print(result)
print(result['result']['Ok'][1][0]['id'])
print(result['result']['Ok'][1][0]['confirmed'])
