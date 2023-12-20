# PYTHON CRYPTO WALLET
## Prerequsites
- Python 3.6 or higher
- Django
- Web3.py

This wallet was built using Django and a web3 library for interacting with the blockchain known as Web3.py. To use this wallet you need to have a virtual environment, python, django, and web3.py installed. If you don't have any of those installed head over to installation to do the needfull 🙂


## Installation
To start the installation you need to check if you have python and pip installed. 
```bash
python3 --version
pip --version
```
Open the terminal and run the following if you don't have it installed:
```bash
sudo apt install python3 && python3-pip
```

If you're using windows, head over to [python's official website](https://python.org/downloads) to download python, pip comes with the python installation...

Install the virtual environment

Mac/Linux/Windows
```bash
pip install virtualenv
```
After the installation, we need to create a virtual environment that will hold the installations of the required packages and activate it:

Mac/Linux:
```bash
virtualenv env_name # The env_name can be anything
. env_name/bin/activate
```
Windows:
```bash
python -m venv env_name # The env_name can be anything
env_name\Scripts\activate
```

Next, clone the repo and cd into it:
```bash
git clone https://github.com/cakezero/wallet.git
cd wallet
```

Let's start the installation of the required stuffs:
```bash
pip install -r requirements.txt
```

And finally run:
```bash
python manage.py migrate
python manage.py runserver
```
Then head over to localhost:8000. To start using the wallet.
