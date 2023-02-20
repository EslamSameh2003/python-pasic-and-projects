import requests
import time
api_key=''
bot_key=''
chat_id=''
limit=59000
time_interval= 5 * 60
def get_pric():
    url='https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '10',
        #'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
    }
    response= requests.get(url,headers=headers,params=parameters).json()
    btc_price=response['data'][0]['quote']['USD']['price']
    return  btc_price

def sent_update(chat_id,msg):
    url=f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}" 
    requests.get(url)

def main():
    while True:

        price=get_pric()
        print(print)
        if price<limit:
          sent_update(chat_id,f"price of bitcoin is : {price}")
        time.sleep(time_interval) 
main()


