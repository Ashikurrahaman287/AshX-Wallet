import requests

def check_balance(address):
    url = f"https://api.blockcypher.com/v1/btc/test3/addrs/{address}/balance"
    response = requests.get(url)
    data = response.json()
    return data['balance']
