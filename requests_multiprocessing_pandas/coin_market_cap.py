import pandas as pd
from multiprocessing_requests import multiprocessing_requests

url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest" 
coin_market_results = multiprocessing_requests(url)
data = pd.DataFrame.from_records(coin_market_results)

print(data['data'].values)
