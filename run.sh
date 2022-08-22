#!/usr/bin/env bash

. venv/bin/activate

python3 src/send_telegram.py

# echo 'get common news'
python3 src/get_news_common.py

# echo 'get cs news'
python3 src/get_news_cs.py

# echo 'get special news'
python3 src/get_news_special.py

python3 src/get_news_ctsv.py
