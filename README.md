# AUTO BOT GET NEWS

This bot will `announce new post` every day from:
* https://student.uit.edu.vn/ 
* https://cs.uit.edu.vn/
* https://ctsv.uit.edu.vn/

This info is being sent to your `Telegram` account.

## My environment: 
```
OS: Ubuntu20.04
Python: 3.8
VPS: 1core-1GB ram (optional)
```

## 1. Clone source code and preparing environment
First, git clone this repo and set up environment: 
```
git clone https://github.com/lynguyenminh/uit_daily_news_bot.git && cd uit_daily_news_bot
```
Then, create virtualenv:
```
virtualenv venv && source venv/bin/activate
pip install -r requirements.txt
```

## 2. Create Telegram bot and add your account
### 2.1. Create Telegram bot
Search `BotFather` and do the following, your bot id is the one I blurred: 
![create-bot-tele](https://user-images.githubusercontent.com/82688630/212620535-a96191e0-dda4-4f81-91bd-d7721ac4f098.png)


### 2.2. Get your account id
Search `userinfobot` and type `/start`

![get-user-id](https://user-images.githubusercontent.com/82688630/212620716-bc73a477-a937-4a55-a66d-2b955ffc0c04.png)


Then fill `bot id` and `account id` into [send_telegram.py](./src/send_telegram.py)

## 3. Run code
I schedule it run one time per day at `1.am`. To do it, i use `crontab`.On Ubuntu, open crontab by `crontab -e`. 
Then write this script: 
```
0 1 * * * /usr/bin/env bash -c 'cd /root/uit_daily_news_bot && sh /root/uit_daily_news_bot/run.sh'
```
If this code has any errors, please create issue or contact me by email: 20521592@gm.uit.edu.vn
