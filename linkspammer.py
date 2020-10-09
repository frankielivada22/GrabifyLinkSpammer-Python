import requests
import random
import time
import sys
import os

askloop = input("How many times do you want to loop: ")
useragent = input(str("user-agent (can be anything): "))
url = input("Grabify link: ")
loop = int(askloop)

print("Starting...")

headers = {
    'authority': 'grabify.link',
    'user-agent': useragent,
}

while loop > 0:
    f = open("proxies.txt", "r")
    prox = f.readline()
    proxy = prox.rstrip("\n")
    proxies = {
        'http': 'http://'+proxy,
        'https': 'https://'+proxy,
    }
    print(proxies)
    response = requests.get(url, headers=headers, proxies=proxies)
    print("Went to", url)
    print(url, "= True", "Looped:", loop, "times", "Used proxie:", proxy) #DEBUG LINE
    loop = loop - 1


time.sleep(5)
