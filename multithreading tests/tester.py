import requests
import random
import time
import sys
import os
import threading

askloop = input("How many times do you want to loop: ")
useragent = input(str("user-agent (can be anything): "))
url = input("Grabify link: ")
loop = int(askloop)

print("Starting...")

headers = {
    'authority': 'grabify.link',
    'user-agent': useragent,
}

def f():
    f = open("proxies.txt", "r")
    prox = f.readline()
    if prox == '':
        print("No proxy was found so ima do my ip instad")
        response = requests.get(url, headers=headers)
        print(response.content)
        print(response)
        print(headers)
        print("Went to", url)
        print(url, "= True", "Looped:", loop, "times") #DEBUG LINE
        return
    else:
        proxy = prox.rstrip("\n")
        proxies = {
            'http': 'http://'+proxy,
            'https': 'https://'+proxy,
        }
        print(proxies)
        response = requests.get(url, headers=headers, proxies=proxies)
        print("Went to", url)
        print(url, "= True", "Looped:", loop, "times", "Used proxie:", proxy) #DEBUG LINE
        return

if __name__ == '__main__':
    for i in range(loop):
        t = threading.Thread(target=f)
        t.start()

