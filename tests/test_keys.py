import unittest
from wallet.keys import generate_new_address

class TestKeys(unittest.TestCase):
    def test_generate_new_address(self):
        address, private_key, public_key = generate_new_address()
        self.assertIsNotNone(address)
        self.assertIsNotNone(private_key)
        self.assertIsNotNone(public_key)

if __name__ == "__main__":
    unittest.main()
