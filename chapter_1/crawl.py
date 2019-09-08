from urllib.request import urlopen #for request to access url and to read that url
from urllib.error import HTTPError
from bs4 import BeautifulSoup
# Beautiful Soap 
#it helps format
#organize the messy web by fixing bad HTML
# and presenting us with easily-traversible Python 
# objects representing XML structures

# html = urlopen("http://pythonscraping.com/pages/page1.html") #complete website

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html") #complete website 
except HTTPError as e:
    print(e)
else:
    Beauty_obj = BeautifulSoup(html.read(),features="html.parser")


print(Beauty_obj.div)





