#!/usr/bin/env python

from PIL import Image
from tqdm import tqdm
import argparse
import math
import praw
import requests
import time
import uuid

# creds of course
username = ''
password = ''
client_id = ''
secret = ''
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

sub = 'all'
search = 'AmateurRoomPorn'
sortby = 'hot'
limit = 5

formats = [
    'image/jpeg',
    'image/jpg',
    'image/png',
    'image/webp',
    'image/gif'
]

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-r', '--subreddit', help='Subreddit to search.')
    p.add_argument('-s', '--search', help='Search term.')
    p.add_argument('-t', '--sort', help='relevance, hot, top, new')
    p.add_argument('-l', '--limit', help='Search limit. Default is 5 and max is 1000', type=int)
    args = p.parse_args()

    sub = args.subreddit if args.subreddit else sub
    search = args.search if args.search else search
    sortby = args.sort if args.sort else sortby
    limit = args.limit if args.limit else limit
    limit = None if limit == 1000 else limit

    reddit = praw.Reddit(client_id=client_id, client_secret=secret, password=password, username=username, user_agent=ua)
    subreddit = reddit.subreddit(sub)

    filenames = []
    session = requests.Session()
    for s in subreddit.search(search, limit=limit):
        url = s.url
        if 'imgur.com/' in url:
            url = url + '.jpg'
        resp = session.get(url, stream=True)

        ct = resp.headers['Content-Type']
        if not ct.startswith('image/') or ct not in formats:
            print(f'ERR: {url} - {ct}')
            continue
        ext = resp.headers['Content-Type'].split('/')[-1]
        tsize = int(resp.headers.get('Content-Length', 0))
        bsize = 1024
        written = 0
        try:
            fname = f'{str(uuid.uuid1())}.{ext}'
            print(f'Downloading {fname}...')
            with open(fname, 'wb') as f:
                for cont in tqdm(resp.iter_content(bsize), total=math.ceil(tsize//bsize), unit='KB', unit_scale=1):
                    written += len(cont)
                    f.write(cont)
            filenames.append(fname)
        except Exception as e:
            print(e)

    # uncomment for autoshowing
    # for fname in filenames:
    #     img = Image.open(fname)
    #     img.show()
    #     while True:
    #         inp = input('Enter to continue...')
    #         if not inp:
    #             break
    #     img.close()
