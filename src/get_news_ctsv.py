from hashlib import new
from bs4 import BeautifulSoup
import urllib.request
from tqdm import tqdm
import json
from send_telegram import *
import asyncio

url =  'https://ctvs.uit.edu.vn/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
domain = ''

class_name = [
    'views-row views-row-1 views-row-odd views-row-first', 
    'views-row views-row-2 views-row-even', 
    'views-row views-row-3 views-row-odd', 
    'views-row views-row-4 views-row-even views-row-last', 
    'views-row views-row-4 views-row-even', 
    'views-row views-row-5 views-row-odd', 
    'views-row views-row-6 views-row-even', 
    'views-row views-row-7 views-row-odd', 
    'views-row views-row-8 views-row-even views-row-last'
]


class uit_feed:
    def __init__(self, title, link) -> None:
        self.title = title
        self.link = link
    
    def compare(self, other_feed):
        return self.title == other_feed.title and self.link == other_feed.link


def get_new(class_name):
    new_feed = soup.find_all('li', class_=class_name)
    list_feed = []
    for i in new_feed:
        i = i.find('a')
        link = domain + str(i.get('href'))
        title = i.getText()
        feed =uit_feed(title=title, link=link)
        list_feed.append(feed)
    return list_feed

def get_new_hot():
    new_feed = soup.find_all('div', class_='top-title')
    list_feed = []
    for i in new_feed:
        i = i.find('a')
        link = domain + str(i.get('href'))
        title = i.getText()
        feed =uit_feed(title=title, link=link)
        list_feed.append(feed)
    return list_feed

def check_in(feed, list_old_feed):
    for i in list_old_feed: 
        if feed.compare(i):
            return True
    return False


# get new feed
list_new_feed = get_new_hot()
for i in tqdm(class_name):
    list_new_feed += get_new(class_name=i)


# read old feed
f = open('data/current_feed_ctsv.json')
data = json.load(f)
f.close()
list_old_feed = [uit_feed(i.get('title'), i.get('link')) for i in data['info']]


#  check new_feed
new_feed = []
for feed in list_new_feed: 
    if not check_in(feed, list_old_feed): 
        new_feed.append(feed)


# send message
new_feed = [i.__dict__ for i in new_feed]
for i in new_feed:
    asyncio.run(send_message(i.get('link')))


# save current feed
list_new_feed = [i.__dict__ for i in list_new_feed]
with open("data/current_feed_ctsv.json", "w", encoding='utf-8') as outfile:
    json.dump({"info":list_new_feed}, outfile, ensure_ascii=False, indent=4)

