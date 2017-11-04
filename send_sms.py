#!/usr/bin/python3
import requests
import sys
import os

url = 'https://cpa-api.kyivstar.ua/api/gateway/public/send'

proxy = {
  'http':'socks5://localhost:9050'}

data = {
  'phone': sys.argv[1],
  'text': sys.argv[2]}

def send_sms():
    os.system('sudo pkill tor')
    os.system("tor > 1& sleep 2")
    return requests.post(url,
                         proxies=proxy,
                         data=data)
try:
    res = send_sms()

    #while 'Limit' in res.text:
    #    res = send_sms()

    print(res.text)

except IndexError:
    print('Require arguments!\n\nExample: sms 380960000000 \'Hello world!\'\n')

