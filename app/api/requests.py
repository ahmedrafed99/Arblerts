import requests

def get_ticker_data(api_key, ticker, convert='USD'):
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={ticker}&convert={convert}'

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data'][ticker]
    else:
        print(f'Request failed with status code {response.status_code}')
