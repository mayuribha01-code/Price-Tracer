import requests
from bs4 import BeautifulSoup


class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
        self.response = requests.get(url, headers={"User-Agent": self.user_agent}).text
        self.soup = BeautifulSoup(self.response, features="html.parser" )

    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag Not Found"

    def product_price(self):
        price = self.soup.find("span", {"class": "a-price-whole"})
        if price is not None:
            return price.text
        else:
            return "Tag Not Found"

device = PriceTracer(url="https://www.amazon.in/Samsung-Awesome-Storage-Nightography-Upgrades/dp/B0GS1F8K8L/ref=sr_1_3?adgrpid=1316117023930291&dib=eyJ2IjoiMSJ9.37vjao5HMmuGZ2aDko-F5dkjMKQuxSrVMeoYsm4PtNrIthzz2rQONlWcZgVaaHZyc1BceKb0wxvcyX-BufMP4Sj5SLu41M3rSY4QV2-Ew8SHI0l6tXrJ4chrvY91M2D3qSfiuZLC6_P82NczUsyLotoX_M7Rcn5FuNc7so98rRYVIOmxGUTI9yuy_AAYXzFi22yaytimtVjUON6PrRrFoHZL-3qq3MY4GH6SgImFwMc.If0-90dOFQAIt1bMZC-VEjKwZGpVoXpfcqbJ_OBGa9U&dib_tag=se&hvadid=82257584793499&hvbmt=bp&hvdev=c&hvlocphy=155127&hvnetw=o&hvqmt=p&hvtargid=kwd-82258188725360%3Aloc-90&hydadcr=25229_2783757&keywords=samsung%2Bphone&mcid=56363367e8ae38818c763fde177cb0e7&msclkid=1da18e829d2d1f3686aee7508a2aebd2&qid=1775376152&sr=8-3&th=1")
print("Device name:", device.product_title())
print("Device price: Ru.",device.product_price())

case = PriceTracer(url="https://www.amazon.in/dp/B0FPR2V6MV/ref=sspa_dk_detail_0?pd_rd_i=B0FPR2V6MV&pd_rd_w=mBumj&content-id=amzn1.sym.67d3dec9-3503-44a1-a945-e969d04cca69&pf_rd_p=67d3dec9-3503-44a1-a945-e969d04cca69&pf_rd_r=VVM1TQ7NQJCY65F34ZSG&pd_rd_wg=DlJaK&pd_rd_r=917b9f7e-96fb-4634-87e4-f20d56167296&aref=2MAAb180WT&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1")
print("Case price: Ru.", case.product_price())
