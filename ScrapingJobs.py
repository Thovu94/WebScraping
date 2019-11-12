from bs4 import BeautifulSoup
import requests

url = "https://ca.indeed.com/Web-Developer-jobs"
response = requests.get(url)

data = response.text
soup = BeautifulSoup(data, "html.parser")
titles = soup.find_all("a", {"class": "jobtitle turnstileLink"})
locations = soup.find_all("div", {"class":"location accessible-contrast-color-location"})
ratings = soup.find_all("span", {"class": "ratingsContent"})
dates = soup.find_all("span", {"class": "date"})
count = 0
for title, location, date in zip(titles, locations, dates):
    count += 1
    print("Position:{}".format(title.text))
    print("Location:{}".format(location.text))
    print("Posted:{}".format(date.text))
    print("--------------------------------------")
    
print("Total jobs are: {}".format(count))

    