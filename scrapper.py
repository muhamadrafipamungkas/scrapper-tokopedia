import requests
from bs4 import BeautifulSoup, Tag

class ScrapperTokopedia:
    url = None
    price = None

    def __init__(self, url):
        self.url = url
    def getPrice(self):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
            s = requests.Session()
            page = s.get(self.url, headers = headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            self.price = soup.find(attrs={"css-c820vl"}).get_text()
            print(self.price)

        except:
            print("Gagal")