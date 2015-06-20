#!/usr/bin/python2
# -*- coding: utf-8 -*-
# by: pantuts
# Get all proxies from
# ip-adress.com/proxy_list
# proxy-list.prg

import re
import requests
from bs4 import BeautifulSoup

PROXIES = []

def get_soup(url):
    try:
        headers = { 'user-agent': 'Firefox' }
        req = requests.get(url, headers=headers, timeout=20, allow_redirects=True)
        soup = BeautifulSoup(req.text, 'html.parser')
        return soup
    except Exception, e:
        print str(e)
        return False


def get_proxies(soup, stype):
    global PROXIES

    if stype == 'adress':
        for i in soup.find_all('tr', attrs={'class': ['odd', 'even']}):
            PROXIES.append(i.next.next.text)
    elif stype == 'listorg':
        for i in soup.find_all('li', attrs={'class': 'proxy'}, text=re.compile(r'[0-9]')):
            PROXIES.append(i.get_text())
    else:
        pass


def write_file(data):
    with open('proxies.txt', 'w') as f:
        for d in data:
            f.write(d + '\n')


if __name__ == '__main__':
    print 'Pantuts :)'

    # ip-adress
    print 'Proxies for: ip-adress.com'
    soup = get_soup('http://www.ip-adress.com/proxy_list/')
    if soup:
        get_proxies(soup, 'adress')

    # proxy-list.org
    print 'Proxies for: proxy-list.org'
    for i in range(10):
        print 'Page ' + str(i + 1)
        soup = get_soup('http://proxy-list.org/english/index.php?p=' + str(i + 1))
        if soup:
            get_proxies(soup, 'listorg')

    print 'Okiedokie!'
    write_file(PROXIES)
