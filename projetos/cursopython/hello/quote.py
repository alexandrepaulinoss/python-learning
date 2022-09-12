import requests
from datetime import datetime

urlDollar = 'https://economia.awesomeapi.com.br/all/USD-BRL'
urlEuro = 'https://economia.awesomeapi.com.br/all/EUR-BRL'

print(
    f'Requesting Dollar and Euro quote in {datetime.now().strftime("%m/%d/%Y at %H:%M:%S")}...')


responseDollar = requests.get(urlDollar)

if responseDollar.status_code == 200:
    dollar_response = responseDollar.json()
    dollar_quote = dollar_response['USD']['low']
    dollar_quote_date = datetime.strptime(
        dollar_response['USD']['create_date'], '%Y-%m-%d %H:%M:%S')
    print(
        f'The Dollar was quoted R$ {float(dollar_quote):.2f} in {dollar_quote_date.strftime("%m/%d/%Y at %H:%M:%S")}')
else:
    print('Error fetching Dollar quote!')


responseEuro = requests.get(urlEuro)

if responseEuro.status_code == 200:
    euro_response = responseEuro.json()
    euro_quote = euro_response['EUR']['low']
    euro_quote_date = datetime.strptime(
        euro_response['EUR']['create_date'], '%Y-%m-%d %H:%M:%S')
    print(
        f'The Euro was quoted R$ {float(euro_quote):.2f} in {euro_quote_date.strftime("%m/%d/%Y at %H:%M:%S")}')
else:
    print('Error fetching Euro quote!')

print(
    f'Quote request finished in {datetime.now().strftime("%m/%d/%Y at %H:%M:%S")}.')
