
# AshX Wallet

AshX Wallet is a basic cryptocurrency wallet built in Python for managing Bitcoin transactions on the Bitcoin testnet. It allows users to generate addresses, check balances, and send transactions.

## Features

- Generate new Bitcoin addresses (public and private keys)
- Check the balance of a Bitcoin address
- Create, sign, and broadcast Bitcoin transactions

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/AshX_Wallet.git
   cd AshX_Wallet
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script to start the AshX Wallet application:

   ```bash
   python main.py
   ```

2. Follow the on-screen instructions to:
   - Generate a new address
   - Check the balance of an address
   - Send a Bitcoin transaction

## Project Structure

```
AshX_Wallet/
├── README.md
├── requirements.txt
├── main.py
├── wallet/
│   ├── __init__.py
│   ├── keys.py
│   ├── transactions.py
│   ├── utils.py
└── tests/
    ├── __init__.py
    ├── test_keys.py
    ├── test_transactions.py
```

- **README.md**: Project description and setup instructions.
- **requirements.txt**: List of required Python libraries.
- **main.py**: Main script to run the AshX Wallet application.
- **wallet/**: Package containing modules for key management, transaction handling, and utility functions.
  - **keys.py**: Functions for generating and managing public/private keys.
  - **transactions.py**: Functions for creating, signing, and broadcasting transactions.
  - **utils.py**: Helper functions (e.g., balance checking).
- **tests/**: Unit tests for the wallet functionalities.
  - **test_keys.py**: Tests for the key management functions.
  - **test_transactions.py**: Tests for the transaction functions.

## Running Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to update the tests as appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [bitcoinlib](https://github.com/1200wd/bitcoinlib) for Bitcoin operations in Python
- [blockcypher](https://www.blockcypher.com/) for blockchain data APIs
