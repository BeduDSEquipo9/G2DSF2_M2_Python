import requests
from bs4 import BeautifulSoup

url = "https://www.zillow.com/homes/for_rent/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

rental_properties = soup.find_all("div", class_="list-card-info")

for rental_property in rental_properties:
    price = rental_property.find("div", class_="list-card-price").text
    address = rental_property.find("address").text

    print("Price:", price)
    print("Address:", address)
    print("---" * 20)
