from bs4 import BeautifulSoup
import requests

# HTML From File
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#print(doc.prettify())
# print(doc.title)
# print(doc.title.string)
# doc.title.string="Hello Ammar" 
# print(doc.title)

tags = doc.find_all("p")[0]
print(tags)
print("**"*20)
#print(tags.find_all("b"))

# HTML From Website
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)

######################################################################################

from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

###################################################    
tags = doc.find_all("input", type="text")

for tag in tags:
    tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(doc))
###################################################

tags=doc.find_all(["p","li","div"])
 
tags=doc.find_all("option",text="Undergraduate",value="undergraduate")

tags=doc.find_all(class_="btn-item")
print(tags)

tags=doc.find_all(text=re.compile("\$.*"),limit=1)

for tag in tags:
    print(tag.strip())
    
##############################################################
    
from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody

trs = tbody.contents

# print(trs[0].next_sibling)
# print(trs[1].previous_sibling)
#trs[0].next_siblings returns an iterator
##trs[0].parent! the parent tag..parent.name gives the name 
## trs[0].descendents gives an iterator for descendents
## children also similar to descendents

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

print(prices)


#######################################################################################

