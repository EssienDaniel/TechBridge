import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"

fetch_data = requests.get(url).content

soup = BeautifulSoup(fetch_data, features="html.parser")

header = soup.find("tr",{"class":"sorttop"})
# location = header.find("th",{"class":"covid-country-narrow-on-mobile"}).text.replace("[a]","")
# cases = header.find("th",{"class":"covid-country-narrow-on-mobile"}).text.replace("[a]","")
# print(location.replace("[a]",""))

print(header)
print("-"*50)
print(f"Location".center(10), f"Cases".center(10), f"Deaths".center(10), f"Recoveries".center(15), sep="|")
print("-"*50)


for val in header.find_all("th"):
    name= val[1].text
    case1 = val[2].text
    death1 = val[3].text
    recovery1 = val[4].text

print(f"{name}".center(10), f"{case1}".center(10), f"{death1}".center(10), f"{recovery1}".center(15), sep="|")

#print(list1)
#print("-"*50)

#print(f"{location}".center(10), f"{case}".center(10), f"{death}".center(10), f"{recoveries}".center(15), sep="|")