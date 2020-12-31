import scrapy
import json


class CoinbaseSpider(scrapy.Spider):
    name = 'coinbase'
    allowed_domains = ['coinbase.com']
    start_urls = ['https://www.coinbase.com/price/']

    def parse(self, response):
        with open('link.json', 'r') as mahn:
            outer_link = json.load(mahn)
            for link in outer_link:
                url = link.get('link')
                yield scrapy.Request(url = url, callback= self.parse_detail)
    
    def parse_detail(self, response):
        raw_data = response.body
        items = json.loads(raw_data)
        for item in items.get("data"):
            title = item.get("name")
            market_cap = item.get("market_cap")
            price = item.get("latest")
            change = item.get("latest_price").get("percent_change").get("day")
            yield {
                "name": title,
                "Market Cap": market_cap,
                "Price": price,
                "change": change

            }

            
