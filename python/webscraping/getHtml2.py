from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html, "html.parser")
# nameList = bsobj.findAll("span", {"class" : "green"})
nameList = bsobj.findAll({"h1", "h2", "h3", "h4", "h5", "h6"})

for name in nameList:
    print(name.get_text())