from hashlib import new
from bs4 import BeautifulSoup
import urllib.request
from tqdm import tqdm
import json
from send_telegram import *
import asyncio

url =  'https://cs.uit.edu.vn/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')


class uit_feed:
    def __init__(self, title, link) -> None:
        self.title = title
        self.link = link
    
    def compare(self, other_feed) -> bool:
        return self.title == other_feed.title and self.link == other_feed.link


def check_in(feed, list_old_feed) -> bool:
    for i in list_old_feed: 
        if feed.compare(i):
            return True
    return False


class_name = 'entry-header'
new_feed = soup.find_all('div', class_=class_name)

# detect current feed
list_new_feed = []
for i in tqdm(new_feed):
    feed = i.find_all('a')
    link = feed[1].get('href')
    title = feed[1].getText()
    list_new_feed.append(uit_feed(title=title, link=link))


# read old feed
f = open('data/current_feed_cs.json')
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
with open("data/current_feed_cs.json", "w", encoding='utf-8') as outfile:
    json.dump({"info":list_new_feed}, outfile, ensure_ascii=False, indent=4)

