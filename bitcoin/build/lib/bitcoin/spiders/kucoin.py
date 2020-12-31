import scrapy
import json


class KucoinSpider(scrapy.Spider):
    name = 'kucoin'
    allowed_domains = ['www.kucoin.com']
    start_urls = ['https://www.kucoin.com/markets/']
  

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Ref": "https://www.kucoin.com/markets",
        "Sec-fetch-dest": "empty",
        "Sec-fetch-mode": "cors",
        "Sec-fetch-site": "same-origin",
        "Aser-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

    }

    def parse(self, response):
        url = 'https://www.kucoin.com/_api/trade-front/market/getSymbol/BTC?lang=en_US&_t=1608711291483'
        yield scrapy.Request(url=url, callback=self.parse_detail, headers=self.headers)

    def parse_detail(self, response):
        raw_data = response.body
        items = json.loads(raw_data)
        for item in items.get("data"):
            title = item.get("symbol")
            amount = item.get("vol")
            valume = item.get("volValue")
            last_trade_price = item.get("averagePrice")
            Hchange = item.get("changeRate")
            last_price = item.get("sell")
            yield {
                "Titile": title,
                "Amount(24H)": amount,
                "Volume(24H)":valume,
                "Refrence AVG Price": last_trade_price,
                "24H Change": Hchange,
                "Last Price": last_price
            }

