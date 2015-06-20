#!/usr/bin/python2
# -*- coding: utf-8 -*-
# by: pantuts
# Get all proxies from ip-adress.com/proxy_list

import requests
from bs4 import BeautifulSoup


def get_soup(url):
    try:
        headers = { 'user-agent': 'Firefox' }
        req = requests.get(url, headers=headers, timeout=20, allow_redirects=True)
        soup = BeautifulSoup(req.text, 'html.parser')
        return soup
    except Exception, e:
        print str(e)
        return False


def get_proxies(soup):
    for i in soup.find_all('tr', attrs={'class': ['odd', 'even']}):
        print i.next.next.text


if __name__ == '__main__':
    print 'Pantuts :)'
    soup = get_soup('http://www.ip-adress.com/proxy_list/')
    if soup:
        get_proxies(soup)
        
# just run: python2 proxy_list.py
