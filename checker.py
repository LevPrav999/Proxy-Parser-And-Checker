import requests
from threading import Thread
from time import time
from random import choice


result = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
                  "AppleWebKit/537.36 (KHTML, like Gecko) " +
                  "Chrome/70.0.3538.77 Safari/537.36"
}
urls = [
    'https://www.google.com.ru/',
    'https://ya.ru/',
    'https://github.com/',
    'https://vk.com/'
]


def processing_check(proxy):
    proxies = {
        "https": proxy,
        "http": proxy
    }
    start_time = time()
    try:
        requests.get(
            choice(urls),
            proxies=proxies,
            headers=headers,
        )
    except requests.exceptions.ProxyError:
        print("[ERROR] Cannot connect to proxy.")
    except Exception as e:
        print(f"[ERROR] {e}")

    return print(
        "[VALID] Proxy: " + proxy + " Time: " + str(
            round(time() - start_time, 2)
        )
    )


def start_checking(list_p):
    for proxy in list_p:
        Thread(target=processing_check, args=(proxy, )).start()
