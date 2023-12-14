from django.shortcuts import render
from web3 import Web3
from dotenv import loadenv
from aiohttp import request
from django.contrib.auth.decorators import login_required
import requests
loadenv()

# Create your views here. To us the env it's os.getenv('Whatever you name it')

def home(request):
    return render(request, 'crypto_wallet/home.html')

def new_account(request):
    return render(request, 'crypto_wallet/new_account.html')

def balance(request, address):
    return render(request, 'cypto_wallet/balance.html')

def send_tx(request):
    return render(request, 'crypto_wallet/send_tx.html')

def market_data(request, address, days):
    return render(request, 'crypto_wallet/market_chart.html')