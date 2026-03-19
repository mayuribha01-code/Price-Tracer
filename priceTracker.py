import requests
from bs4 import BeautifulSoup
class PriceTracker:

    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-Language": "en-US,en;q=0.9"
        }
        self.soup = None
        self.getPage()

    def getPage(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raisForStatus()
            self.soup = BeautifulSoup(response.text, "html.parser")
        except Exception as e:
            print("Error fetching page:", e)

    def getTitle(self):
        if self.soup:
            title = self.soup.find("span", id="productTitle")
            if title:
                return title.text.strip()
        return "Title not found"

  
    def getPrice(self):
        if self.soup:
            price = self.soup.find("span", class_="a-offscreen")
            if price:
                return price.text.strip()
        return None


    def getPriceValue(self):
        price = self.getPrice()
        if price:
            price = price.replace("₹", "").replace(",", "")
            try:
                return float(price)
            except:
                return None
        return None


    def checkPrice(self, targetPrice):
        currentPrice = self.getPriceValue()

        if currentPrice is None:
            print("Price not available")
            return

        print("Current Price: ₹", currentPrice)

        if currentPrice <= targetPrice:
            print("Alert! Price dropped below your target")
        else:
            print("Price is still higher than target")

url = "https://www.amazon.in/dp/B0DSBVGKVF"

tracker = PriceTracker(url)

print("Product:", tracker.getTitle())

tracker.checkPrice(1500)
