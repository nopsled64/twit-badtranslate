from googletrans import Translator
import random
import config
import tweepy
import os

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.token_secret)
#api = twitter.Api(consumer_key=config.consumer_key, consumer_secret=config.consumer_secret, access_token_key=config.access_token, access_token_secret=config.token_secret)
api = tweepy.API(auth)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def bad_translate(quote):
    print("Translating into French...")
    quote = translator.translate(quote, dest="fr").text
    print("Translating into Romanian...")
    quote = translator.translate(quote, dest="ro").text
    print("Translating into Indonesian...")
    quote = translator.translate(quote, dest="id").text
    print("Translating into Malagasy...")
    quote = translator.translate(quote, dest="mg").text
    print("Translating into Igbo...")
    quote = translator.translate(quote, dest="ig").text
    print("Translating into Greek...")
    quote = translator.translate(quote, dest="el").text
    print("Translating into Russian...")
    quote = translator.translate(quote, dest="ru").text
    print("Translating into Kurdish (Kurmanji)...")
    quote = translator.translate(quote, dest="ku").text
    print("Translating into Hebrew...")
    quote = translator.translate(quote, dest="he").text
    print("Translating into Filipino...")
    quote = translator.translate(quote, dest="fil").text
    print("Translating into Marathi...")
    quote = translator.translate(quote, dest="mr").text
    print("Translating into Italian...")
    quote = translator.translate(quote, dest="it").text
    print("Translating back into English...")
    quote = translator.translate(quote, dest="en").text
    return quote

def delete_line(filename, line_number):
    newdata = "mynewstring"
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        del lines[line_number]
    print("Deleting line", line_number)
    with open(filename,'w') as f:
        f.write('\n'.join(lines))

translator = Translator()
quotefile = "quotes.txt"

print("Determining quotefile size...")

quotefile_len = file_len(quotefile)

print("Quotefile size is", quotefile_len,"lines.")

with open(quotefile) as f:
    quote_list = f.readlines()
quote_list = [x.strip() for x in quote_list]

while True:
    daily_quote_number = random.randint(1,quotefile_len)

    quote_body = quote_list[daily_quote_number]

    print("Today's quote is: \"",quote_body,"\"", sep='')

    bad_quote = bad_translate(quote_body)

    #bad_quote = "test"

    print("\"", bad_quote,"\"", sep='')

    if len(bad_quote) < 280:
        api.update_status(bad_quote)
        print("Posted to Twitter!")
        delete_line(quotefile,daily_quote_number)
        break

    delete_line(quotefile,daily_quote_number)
