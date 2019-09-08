#define a function to get the title of specific website

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def find_title(url):
    try:
        responce = urlopen(url) #complete website)
        if responce is "None":
            print("Url does not exist")
    except HTTPError as e:
        print(e)
    try:
        website_data = BeautifulSoup(responce.read(),features="html.parser")
       # print(website_data.p) # return an None because this url does  not have tag p
        print(website_data.h1)        
    except AttributeError as attr:
        print(attr)    
   
# find_title("http://pythonscraping.com/pages/page1.html")
# find_title("http://flexstudent.nu.edu.pk/Login")

def find_all_span(url):
    
    responce = urlopen(url)
    # except HTTPError as e:
    #     print(e)
    BS_obj = BeautifulSoup(responce,features="html.parser")
    All_Spans_list = BS_obj.findAll("span", {"class:green"})     # find_all("tagName",{"CSS Property"}) and it returns in a python List  
    for i in All_Spans_list:
        print(i.get_text())

find_all_span("http://www.pythonscraping.com/pages/warandpeace.html")    



