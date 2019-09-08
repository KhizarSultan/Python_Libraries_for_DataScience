# extract the links form wikipidia

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    data = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
except HTTPError as e:
    print(e) 
else:
    bs_obj = BeautifulSoup(data,features="html.parser")
    all_links = bs_obj.findAll("a") # will return dictionary
    for link in all_links:
        if 'href' in link.attrs:
            print(link.attrs['href'])