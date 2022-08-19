from hashlib import new
from bs4 import BeautifulSoup
import urllib.request
from tqdm import tqdm
import json
from send_telegram import *
import asyncio

url =  'https://student.uit.edu.vn/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
domain = 'https://student.uit.edu.vn/'

class_name = [
    'row-1 row-first', 
    'row-2', 
    'row-3', 
    'row-4', 
    'row-5', 
    'row-6', 
    'row-7', 
    'row-8', 
    'row-9', 
    'row-10 row-last'
]


class uit_feed:
    def __init__(self, title, link) -> None:
        self.title = title
        self.link = link
    
    def compare(self, other_feed):
        return self.title == other_feed.title and self.link == other_feed.link


def get_new(class_name):
    new_feed = soup.find('tr', class_=class_name).find('a')
    link = domain + new_feed.get('href')
    title = new_feed.getText()
    feed =uit_feed(title=title, link=link)
    return feed


def check_in(feed, list_old_feed):
    for i in list_old_feed: 
        if feed.compare(i):
            return True
    return False


# get new feed
list_new_feed = []
for i in tqdm(class_name):
    list_new_feed.append(get_new(class_name=i))

# list_new_feed = [i.__dict__ for i in list_new_feed]
# print(list_new_feed)
# read old feed
f = open('data/current_feed_special.json')
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
with open("data/current_feed_special.json", "w", encoding='utf-8') as outfile:
    json.dump({"info":list_new_feed}, outfile, ensure_ascii=False, indent=4)

