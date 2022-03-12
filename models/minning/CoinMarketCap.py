import Model
from requests import get
import sys
import json
import pandas as pd

class CointMarketCap(Model):
    def __init__(self, delay, update_size=100, init_size=100000):
        # Initial Variable
        self.delay = delay
        self.__isUpdate = False
        # Declare size of fetch data
        self.update_size = update_size
        self.init_size = init_size
        # news api of CoinMarketCap.com 
        self.__url = 'https://api.coinmarketcap.com/content/v3/news?'
    
    # Single Process
    def init(self):
        print('Coin Market Cap...')
        data = self.__fetch(self.init_size)
        self.__preprocess(data)

    """
    Update Process
    @Parameter:
        count -> input the second, minute, hour
    """
    def update(self, count):
        if count % self.delay == 0 and self.__isUpdate == False:
            data = self.__fetch(self.update_size)
            self.__preprocess(data)
            self.__isUpdate = True

        elif count % self.delay != 0:
            self.__isUpdate = False


    # Fetch to the API with size
    def __fetch(self, size):
        resp = get(self.__url + f"size={size}")
        json_encoded = json.loads(resp.text)
        data = json_encoded['data']
        return data

    # Preprocess Data
    def __preprocess(self, raw):
        data = {
                #'slug':[],
                'title':[],
                'subtitle':[],
                'source_name':[],
                'source_url':[],
                'assets':[],
                'cover':[],
                'created_at':[]
                }

        for item in raw:
            data['created_at'].append(item['createdAt'] if 'createdAt' in item.keys() else '')
            data['title'].append(item['meta']['title'] if 'title' in item['meta'].keys() else '')
            data['subtitle'].append(item['meta']['subtitle'] if 'subtitle' in item['meta'].keys() else '')
            data['source_name'].append(item['meta']['sourceName'] if 'sourceName' in item['meta'].keys() else '')
            data['source_url'].append(item['meta']['sourceUrl'] if 'sourceUrl' in item['meta'].keys() else '')
            data['cover'].append(item['meta']['cover'] if 'cover' in item['meta'].keys() else '')
            data['assets'].append(item['assets'])
            #data['slug'].append(item['slug'])

        df = pd.DataFrame(data=data)
        #df.set_index('slug', inplace=True)
        print(df.head())

sys.modules[__name__] = CointMarketCap
