#%%
import warnings
import requests
import pandas as pd
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from typing import List
import random
import sys  
possible_agents =  [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
]
def random_headers():
    agent = random.choice(possible_agents)
    return {'User-Agent': agent}
if random_headers() is  None: warnings.warn(f"error at {__file__}'s line {sys._getframe().f_lineno}")
if requests.get('https://www.bing.com', proxies=None, headers=random_headers()) is  None: warnings.warn(f"error at {__file__}'s line {sys._getframe().f_lineno}")
#%%
import time
import requests
def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()
def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
get_proxy()

def get_html(url, retry_count=5, proxy_retry_count=5, retry_interval=0.3, **kargs):
    def try_new_proxy(url,  proxy_retry_count=5):
        if random.random()<0.1:
            proxy = None
        else:
            proxy = get_proxy().get('proxy')
        proxies={"http": "http://{}".format(proxy)} if proxy is not None else None
        while proxy_retry_count>0:
            try:
                html = requests.get(url, proxies=proxies, headers=random_headers(), **kargs)
                return html
            except Exception as e:
                proxy_retry_count-=1
        if proxy is not None:
            delete_proxy(proxy)
        return None
                    
    while retry_count>0:
        html = try_new_proxy(url, proxy_retry_count)
        if html != None: return html
        retry_count-=1
        time.sleep(retry_interval)
    return None
if get_html('https://www.bing.com') is  None: warnings.warn(f"error at {__file__}'s line {sys._getframe().f_lineno}")
