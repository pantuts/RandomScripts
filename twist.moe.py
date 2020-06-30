from tqdm import tqdm
from urllib.parse import unquote
import math
import os
import requests
import sys

ref = sys.argv[1] # https://twist.moe/a/kingdom/
url = sys.argv[2] # https://edge-26.cdn.bunny.sh/anime/kingdom/[A-Destiny]%20Kingdom%20-%2006%20(1280x720%20Hi10p%20AAC)%20[4DA63282].mp4
ep = sys.argv[3]  # 6
fname = unquote(url).split('/')[-1]

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'dnt': '1',
    'Host': list(filter(None, url.split('/')))[1],
    'Referer': f'{ref}{ep}',
    'Sec-Fetch-Dest': 'video',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
session = requests.Session()
resp = session.get(url, headers=headers, stream=True)

try:
    with tqdm.wrapattr(open(fname, 'wb'), 'write',
                   miniters=1, desc=fname,
                   total=int(resp.headers.get('content-length', 0))) as fout:
        for chunk in resp.iter_content(chunk_size=4096):
            fout.write(chunk)
except Exception as e:
    print(e)
