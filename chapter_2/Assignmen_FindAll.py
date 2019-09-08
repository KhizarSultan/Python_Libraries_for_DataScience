from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from bs4 import re # for regular expression

# try:
#     data = urlopen("http://www.pythonscraping.com/pages/page3.html")
# except HTTPError as e:
#     print(e)
# else:
#     bs_obj = BeautifulSoup(data,features="html.parser")
#     my_table = bs_obj.find("table",{"id":"giftList"}) # will return list because we are getting text not attributes
#     for row in my_table:
#         print(row)

try:
    data = urlopen("http://www.pythonscraping.com/pages/page3.html")
except HTTPError as e:
    print(e)
else:
    bs_obj = BeautifulSoup(data,features="html.parser")
    all_images = bs_obj.find_all("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})# will return dictionary bcz we are accessing attributes
          # find_all("tag",{"key:value"} just like dictionary in python)
    for image in all_images:
        print(image['src'])



        
