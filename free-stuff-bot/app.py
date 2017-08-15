#!/usr/bin/env python

import os
import sys

from chalice import Chalice
from lxml import html
import requests

PAGE_URL = 'https://www.packtpub.com/packt/offers/free-learning'
PAGE_XPATH = '//*[@id="deal-of-the-day"]/div/div/div[2]/div[2]/h2/text()'
USER_AGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 ' 
              '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57')
WEBHOOK_URL = os.environ['WEBHOOK_URL']

app = Chalice(app_name='free-stuff-bot')

@app.schedule(Cron(30, 23, '*', '*', '?', '*'))
def handler(event):
    headers = {
        'User-Agent': USER_AGENT
    }

    page = requests.get(PAGE_URL, headers=headers)

    tree = html.fromstring(page.content)
    title = tree.xpath(PAGE_XPATH)

    if title:
        title = title[0].strip()
    else:
        sys.exit(1)

    msg_body = '*Free eBook*\n\n%s\n\n%s' % (title, PAGE_URL)

    msg = {
        'text': msg_body
    }

    resp = requests.post(WEBHOOK_URL, json=msg)

    return resp.status_code
