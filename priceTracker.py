import requests
from bs4 import BeautifulSoup

class PriceTracker:
    def __init__(self, url):
        self.url = url
        self.agent = {'User-Agent': 'Mozilla/5.0'}
        self.response = requests.get(self.url, headers=self.agent).text
        self.soup = BeautifulSoup(self.response, 'html.parser')

    def product_title(self):
        title = self.soup.find("span", id="productTitle")
        if title:
            return title.text.strip()
        else:
            return "Tag not found"

    def product_price(self):
        price = self.soup.find("span", class_="a-price-whole")
        if price:
            return price.text.strip()
        else:
            return "Price not found"


device = PriceTracker(
    url="https://www.amazon.in/dp/B0DSBVGKVF"
)

print(device.product_title())
print(device.product_price())