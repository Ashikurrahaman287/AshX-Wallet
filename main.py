from wallet.keys import generate_new_address
from wallet.transactions import create_and_sign_transaction, broadcast_transaction
from wallet.utils import check_balance

def main():
    print("Welcome to AshX Wallet")
    print("1. Generate New Address")
    print("2. Check Balance")
    print("3. Send Transaction")
    choice = input("Choose an option: ")

    if choice == "1":
        address, private_key, public_key = generate_new_address()
        print("Private Key:", private_key)
        print("Public Key:", public_key)
        print("Address:", address)
    elif choice == "2":
        address = input("Enter your address: ")
        balance = check_balance(address)
        print("Balance:", balance)
    elif choice == "3":
        from_address = input("From Address: ")
        to_address = input("To Address: ")
        amount = int(input("Amount (in satoshis): "))
        fee = int(input("Fee (in satoshis): "))
        private_key = input("Private Key: ")
        tx = create_and_sign_transaction(private_key, from_address, to_address, amount, fee)
        tx_hex = tx.as_hex()
        response = broadcast_transaction(tx_hex)
        print("Transaction Broadcast Response:", response)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
