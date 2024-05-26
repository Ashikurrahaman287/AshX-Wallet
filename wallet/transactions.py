import requests
from bitcoinlib.transactions import Transaction

def create_and_sign_transaction(private_key, from_address, to_address, amount, fee):
    tx = Transaction(network='testnet')
    tx.add_input(from_address, amount + fee, private_key)
    tx.add_output(to_address, amount)
    tx.sign(private_key)
    return tx

def broadcast_transaction(tx_hex):
    url = "https://api.blockcypher.com/v1/btc/test3/txs/push"
    response = requests.post(url, json={'tx': tx_hex})
    return response.json()
