import requests
from bs4 import BeautifulSoup
from main import init_database, add
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=iphone+x&_sacat=0&_odkw=iphone+xmas&_osacat=0"
response = requests.get(url)
content = BeautifulSoup(response.text, "html.parser")
for x in content.find_all("li", {"class": "s-item s-item__pl-on-bottom"}):
    check = x.find("span", {"role": "heading"})
    name = check.text.strip()
    price = x.find("span", {"class": "s-item__price"})
    y = price.text.strip()
    link = x.find('a')
    if link:
        url =  link.get('href')
        init_database()
        add(name, y, url)
    

