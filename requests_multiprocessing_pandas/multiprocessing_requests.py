from requests import Request, Session
import multiprocessing.dummy as mp
import json


def multiprocessing_requests(url):
    token_list = ['bitcoin', 'ethereum','cardano','polkadot']
    api_key = “"
    def requests_pool(token):
        parameters = { 'slug': '{}'.format(token), 'convert': 'USD' }
        headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': '{}'.format(api_key)
                }
        session = Session()
        session.headers.update(headers)
        response = session.get(url, params=parameters)
        print(response.status_code)
        info = json.loads(response.text)
        return info

    with mp.Pool(5) as pool:
        results = [x for x in pool.imap_unordered(requests_pool, token_list , chunksize=16)]
    return results





