# project
import random
import string
print(random.randint(5,10))
letters=string.ascii_lowercase
print(letters)
URLS_DB={}
def get_short_url(url):
    # Convert a long url to short url and save in the database
    l=random.randint(4,6)
    short_url="as.in/"
    for i in range(l):
        short_url+=random.choice(letters)
    if URLS_DB.get(short_url):
        # invalid short url
        return get_short_url(url)
    else:
        URLS_DB[short_url] = url
    return short_url
def get_long_url(short_url):
    #convert short url into long url or will give the long url corresponding to the short url
    if URLS_DB.get(short_url) is None:
        return "Short url doesn't exist"
    else:
        return URLS_DB[short_url]
my_url='https://www.youtube.com/watch?v=dWmM4-TUmQA'
get_short_url(my_url)
