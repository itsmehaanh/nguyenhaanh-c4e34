from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
url = 'https://www.apple.com/itunes/charts/songs/'
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode('utf8')

soup = BeautifulSoup(content,"html.parser")
ul = soup.find("ul","")

li_list = ul.find_all("li")

empty_list = []
# print(li_list)
for li in li_list:
    dic = OrderedDict({"Name":None, "Artist":None})
    a = li.h3.a
    a1= li.h4.a
    name = a.string.strip() 
    print(name)
    # print(a)
    artist = a1.string.strip()
    
    dic["Name"] = name
    dic["Artist"] = artist
    dic = empty_list.append(dic)






# 4. Save data
import pyexcel

  

    

pyexcel.save_as(records=empty_list, dest_file_name="Itunes.xlsx")




  

    


