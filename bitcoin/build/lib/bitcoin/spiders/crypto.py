import scrapy
import json



class CryptoSpider(scrapy.Spider):
    name = 'crypto'
    allowed_domains = ['crypto.com']
    start_urls = ['https://crypto.com/price/']
   

    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Rer": "https://crypto.com/price/",
        "Sec-fetch-dest": "empty",
        "Sec-fetch-mode": "cors",
        "Sec-fetch-site": "same-origin",
        "Aser-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    def parse(self, response):
        url = 'https://crypto.com/price/coin-data/summary/by_market_cap_page_1.json'
        yield scrapy.Request(url=url, callback=self.parse_detail, headers=self.headers)

    def parse_detail(self, response):
        raw_data = response.body
        items = json.loads(raw_data)
        total_page = items.get('page_count')
        for item in items.get('tokens'):
            title = item.get('name')
            price = item.get('usd_price')
            market_cap = item.get('usd_marketcap')
            change = item.get('btc_change_24h')
            yield {
                "Title": title,
                "Price": price,
                "Market_Cap": market_cap,
                "24H Change": change


            }
        for i in range(2, total_page):
            next_page = f'https://crypto.com/price/coin-data/summary/by_market_cap_page_{i}.json'
            yield scrapy.Request(url=next_page, callback=self.parse_detail, headers=self.headers)
