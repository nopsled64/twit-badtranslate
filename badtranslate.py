from googletrans import Translator
import random

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

translator = Translator()
quotefile = "quotes.txt"

print("Determining quotefile size...")

quotefile_len = file_len(quotefile)

print("Quotefile size is", quotefile_len,"lines.")

#quotefile = open("quotes.txt", "r")
#print(quotefile.read())

daily_quote_number = random.randint(1,quotefile_len)

with open(quotefile) as f:
    quote_list = f.readlines()

quote_list = [x.strip() for x in quote_list]

quote_body = quote_list[daily_quote_number].partition("~~")[0]
quote_author = quote_list[daily_quote_number].partition("~~")[2]

print("Today's quote is: \"",quote_body,"\" - ", quote_author, sep='')

bad_quote = bad_translate(quote_body)
print("\"", bad_quote,"\" - ", quote_author, sep='')
