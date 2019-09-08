from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    responce = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
except HTTPError as e:
    print(e)
else:
    bs_obj = BeautifulSoup(responce,features="html.parser")
    # print(bs_obj)
    Green_Para_list = bs_obj.findAll("span",{"class":"red"})
    times = bs_obj.findAll(text="the prince")
    all_green = bs_obj.findAll(class_="green") #
    all_green_2 = bs_obj.findAll("",{"class":"green"}) #both are same
    for para in Green_Para_list:
        # print(para) #will return tags and text
        print(para.get_text()) #will return only text
    print(len(times))    
