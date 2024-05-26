import unittest
from wallet.transactions import create_and_sign_transaction, broadcast_transaction
from wallet.keys import generate_new_address

class TestTransactions(unittest.TestCase):
    def test_create_and_sign_transaction(self):
        address, private_key, public_key = generate_new_address()
        to_address = "2N5E3wmd6GRT4Rhws4k2QPAuVHXt7qDht5R"  # Replace with a real testnet address
        amount = 10000  # Amount in satoshis
        fee = 1000  # Fee in satoshis
        tx = create_and_sign_transaction(private_key, address, to_address, amount, fee)
        self.assertIsNotNone(tx)

if __name__ == "__main__":
    unittest.main()
