import scrapy


class StackedSpider(scrapy.Spider):
    name = 'stacked'
    allowed_domains = ['staked.us']
    start_urls = ['https://staked.us/yields/']
   

    def parse(self, response):
        items = response.xpath("//tr[@class = 'FT__row']")
        for item in items:
            title = item.xpath(".//div[@class = 'Coin__name']/text()").get()
            stacked = item.xpath(".//td[@class = 'FT__cell FT__cell--center']/text()").getall()
            nominal_yield = item.xpath(".//td[@class = 'FT__cell FT__cell--yield']/text()").get()
            real_yeild= item.xpath(".//td[@class = 'FT__cell']/text()").get()
            market_cap = item.xpath(".//span[@class = 'Hint']/text()").getall()
            yield {
                "Title": title,
                "Niminal Yield": nominal_yield,
                "Stacked": stacked[0],
                "Inflation": stacked[1],
                "Lock UP": stacked[2],
                "Real Yield": real_yeild,
                "Market Cap": market_cap[0],
                "Daily VOL": market_cap[2]
            }
        
            

