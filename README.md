# AUTO BOT GET NEWS

This bot will announce new post from https://student.uit.edu.vn/ and https://cs.uit.edu.vn/.

## My environment: 
```
OS: Ubuntu20.04
Python: 3.8
VPS: 1core-1GB ram (optional)
```

## How to run this code?
First, git clone this repo and set up environment: 
```
git clone https://github.com/lynguyenminh/uit_daily_news_bot.git
cd uit_daily_news_bot
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
I schedule it run one time per day. To do it, i use crontab.


Open crontab by `crontab -e`. 
Then write this script: 
```
0 1 * * * /usr/bin/env bash -c 'cd /root/uit_daily_news_bot && sh /root/uit_daily_news_bot/run.sh'
```
