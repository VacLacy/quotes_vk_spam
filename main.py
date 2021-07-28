import vk_api
from time import sleep
import requests


token = str(input('vk token: '))
session = vk_api.VkApi(token=token)
url = 'http://api.forismatic.com/api/1.0/'
payload  = {
    'method': 'getQuote', 
    'format': 'json', 
    'lang': 'ru'
    }

def spam_msg(user_id):
    res = requests.get(url, params=payload)
    data = res.json()
    session.method('messages.send', {
        'user_id': user_id,
        'random_id': 0,
        'message': f'''{data['quoteText']}
        {data['quoteAuthor']}
        '''
    })

def set_status():
    res = requests.get(url, params=payload)
    data = res.json()
    session.method('status.set', {
        'text': f'''{data['quoteText']}
        {data['quoteAuthor']}
        '''
    })

if __name__ == '__main__':
    id_ = int(input('id странички для спама цитаток: '))
    while True:
        # spam_msg(532523089)
        # spam_msg(317206595)
        # set_status()
        # sleep(5)

        spam_msg(id_)

        sleep(5)
  