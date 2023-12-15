import os
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse
from web3 import Web3
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required
import requests
import json
load_dotenv()

alchemy_url = os.getenv("ALCHEMY_ETHEREUM_URL")
api_key = os.getenv("ALCHEMY_ETHEREUM_API_KEY")
CG_apiKey=os.getenv("COINGECKO_API_KEY")
web3 = Web3(Web3.HTTPProvider(alchemy_url))

# Create your views here.

with open(settings.JSON_PATH) as f_obj:
    erc20_abi = json.load(f_obj)

def home(request):
    return render(request, 'crypto_wallet/home.html')

@login_required
def new_account(request):
    account = web3.eth.account.create(api_key)
    info = {
        'privateKey': web3.to_hex(account.key),
        'address': account.address
    }
    request.session['info'] = info
    return JsonResponse(info, safe=False)
    
@login_required
def balance(request, coin_address):
    address = request.session['info']['address']
    checksum_address = Web3.to_checksum_address(address)
    print(checksum_address)
    contract = web3.eth.contract(address=coin_address, abi=erc20_abi)
    balance = contract.functions.balanceOf(checksum_address).call()
    return JsonResponse({'balance': balance})

@login_required
def send_tx(request):
    if request.method == "POST":
        data = request.get_json()
        nonce = web3.eth.getTransactionCount(request.session['info']['address'])
        txn_dict = {
            'to': data['to'],
            'value': web3.toWei(data['amount'], 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei('40', 'gwei'),
            'nonce': nonce,
            'chainId': 3
        }
        signed_txn = web3.eth.account.signTransaction(txn_dict, request.session['info']['privateKey'])
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return JsonResponse({'transaction_hash': txn_hash.hex()})
    else:
        return redirect('crypto_wallet:home')

@login_required
def market_data(request, contract_address, days):
    response = requests.get(f'https://api.coingecko.com/api/v3/coins/ethereum/contract/{contract_address}/market_chart?vs_currency=usd&days={days}&api_key={CG_apiKey}')
    return JsonResponse(response.json(), safe=False)

def register(request):
    if request.method == 'GET':
        form  = UserCreationForm()
    else:
        form  = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            auth_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, auth_user)
            return redirect('/')
    context = {'form': form}
    return render(request, 'crypto_wallet/register.html', context)

@login_required
def logout(request):
    return redirect('/')