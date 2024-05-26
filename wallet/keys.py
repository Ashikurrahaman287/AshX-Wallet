from bitcoinlib.keys import HDKey

def generate_new_address():
    key = HDKey()
    private_key = key.private_hex
    public_key = key.public_hex
    address = key.address()
    return address, private_key, public_key
