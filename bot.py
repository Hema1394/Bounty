import requests
import time

API_TOKEN = '6443804057:AAHF7lKEdzL11iZZXy6HYGDFUqRWk9FL8Ao'
CHAT_ID = '-1002299670728'
GIST_URL = 'https://gist.githubusercontent.com/RedBullSecurity/3eb88debcb01759eccf65ec2b799b340/raw/redbull-bug-bounty-scope-rb-only.txt'

previous_urls = []

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)

while True:
    response = requests.get(GIST_URL)
    current_content = response.text
    current_urls = current_content.splitlines()

    new_urls = [url for url in current_urls if url not in previous_urls]
    deleted_urls = [url for url in previous_urls if url not in current_urls]

    if new_urls:
        new_message = "New URLs added:\n" + "\n".join(new_urls)
        send_telegram_message(new_message)
        previous_urls = current_urls

    if deleted_urls:
        deleted_message = "URLs deleted:\n" + "\n".join(deleted_urls)
        send_telegram_message(deleted_message)
        previous_urls = current_urls

    time.sleep(60) # Check every
