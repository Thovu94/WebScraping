from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

scraper = input("Searching: .. ")
keySearch = {"q": scraper}
reQ = requests.get("http://www.bing.com/images/search", params=keySearch)

soup = BeautifulSoup(reQ.text, "html.parser")
getLinks = soup.findAll("a", {"class": "thumb"})

for link in getLinks:
    img_obj = requests.get(link.attrs["href"])
    title = link.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save("img/" + title, img.format)