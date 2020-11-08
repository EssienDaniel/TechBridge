import requests 
from  bs4 import BeautifulSoup 


# SCRAPPING FROM INTERNET RESOURCE FROM A URL
url = "https://www.jumia.com.ng/smartphones/"

jumia_html = requests.get(url).content

soup = BeautifulSoup(jumia_html, features="html.parser")

# GET ALL H3s FROM JUMIA, THIS CORRESPONDS TO THE PRODUCT NAMES
# all_results = soup.find_all("h3")

# for element in all_results:
#     print(element.text)


# GET ALL DIVs FROM JUMIA, THIS CORRESPONDS TO THE PRODUCT PRICES
# all_results = soup.find_all("div")

# for element in all_results:

#     data = element.text
#     if "₦" in data:

#         print(data)

# # GET ALL PRICES FROM JUMIA, USING THE ASSIGNED CLASS NAME 
# all_results = soup.find_all("div",{"class":"prc"})

# for element in all_results:

#     data = element.text
#     if "₦" in data:

#         print(data)

# # GET ALL PRICES FROM JUMIA, USING THE ASSIGNED CLASS NAME 
all_results = soup.find_all("a",{"class":"core"})

file_name = "jumia_prices.csv"
file = open(file_name, "w", errors= "ignore")

def calc_discount(old, new):

    if old == "No Discount..!!": return 0

    old = int(old.replace(",", "").replace("₦", ""))
    new = int(new.replace(",", "").replace("₦", ""))

    return round((( old - new ) / old) * 100, 1)

for element in all_results:

    name = element.find("h3",{"class":"name"}).text
    price = element.find("div",{"class":"prc"}).text
    try:

        discount = element.find("div",{"class":"old"}).text

    except AttributeError:

        discount = "No Discount..!!"

    file.write(f'{name.replace(",", "")},{price.replace(",", "")},{discount.replace(",", "")},{calc_discount(old = discount, new = price)}\n') # WRITE VALUES TO A FILE.

    print("Name     : ", name) 
    print("Price    : ", price)
    print("Discount : ", discount)
    print("% Discou : ", calc_discount(old = discount, new = price), "%")
    print("--------------------------------")


# SCRAPPING FROM SAMPLE HTML FILE


# html = open("index.html", "r").read()

# soup = BeautifulSoup(html, features="html.parser")
# print(soup)

# found_paragraphs = soup.find("p").text #FIND THE FIRST ELEMENT THAT MATCHES QUERY
# print(found_paragraphs) 

# found_paragraphs = soup.find_all("p") #FIND THE all ELEMENT THAT MATCHES QUERY and returns an iterable

# print(found_paragraphs)

# for object in found_paragraphs:
#     print(object.text)