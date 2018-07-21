# twit-badtranslate
Translates quotes multiple times through Google translate, and then posts them to Twitter.

## Prerequisites

### Install tweepy & googletrans:

`pip3 install --user tweepy googletrans`

### Create a config.py file in the following format:

```
consumer_key = ""
consumer_secret = ""
access_token = ""
token_secret = ""
```

These API keys and tokens can be found by creating a Twitter Application at: https://apps.twitter.com/

### Supply a quotes.txt file

This should have each quote on a new line. If you don't have one, simply rename the supplied quotes file!

Enjoy!
