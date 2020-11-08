import requests
#data = requests.get("https://samples.openweathermap.org/data/2.5/weather?q=Lagos,ng&appid=439d4b804bc8187953eb36d2a8c26a02")

#val = data.json()

#print(val[main][]




# fetch = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=2332453&APPID=336b102582e7d317c464efd5e6ac86aa")

# data = fetch.json()
# print(data["city"]["name"])


### FREE APIS


# fetch = requests.get('https://api.ratesapi.io/api/latest')
# data = fetch.json()

# #print(f"base".center(15), f"rates".center(15), f"date".center(15), sep="|")
# #print("-"*80)
# base = data.get('base')
# for key, value in data.get('rates').items():
#     # print(key, value, end=" | ")
#     print(base, 1, key, value, sep= ' | ')


# BEAUTIFUL SOUP


from bs4 import BeautifulSoup
url = "https://www.jumia.com.ng/smartphones/"
jumia_html = requests.get(url).content

soup = BeautifulSoup(jumia_html, features="html.parser")
#price = soup.find_all("div",{"class":"prc"})

file_name = "jumia_prices.csv"
file = open(file_name, "w", errors= "ignore")
all_result = soup.find_all("a",{"class":"core"})

def calc_discount(old, new):
    if old == "No Discount..!!":return 0

    old = int(old.replace(",","").replace("₦",""))
    new = int(new.replace(",","").replace("₦",""))

    return round(((old - new)/old)*100, 1)




for element in all_result:
    
        name = element.find("h3", {"class":"name"}).text
        price = element.find("div", {"class":"prc"}).text

        try:
            discount = element.find("div",{"class":"old"}).text       
        except AttributeError:
            discount = "No Discount..!!"

        file.write(f'{name.replace(",", "")},{price.replace(",", "")},{discount.replace(",", "")},{calc_discount(old = discount, new = price)}\n') # WRITE VALUES TO A FILE.

        print("Name :", name)
        print("Price : ", price ) 
        print("Discount :", discount)
        print("% Discount : ", calc_discount(old=discount, new=price), "%")
        print("----------------------------------------")

#print(price)

#<span dir="ltr" data-price-old="" class="-tal -gy5 -lthr -fs16">₦ 49,990</span>