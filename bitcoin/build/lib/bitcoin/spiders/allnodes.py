import scrapy


class AllnodesSpider(scrapy.Spider):
    name = 'allnodes'
    allowed_domains = ['www.allnodes.com']
    start_urls = ['https://www.allnodes.com/pricing/']
    

    def parse(self, response):
        items = response.xpath("//div[@class = 'pricing-row-mobile pricing-row-mobile__odd']")
        for item in items:
            title = item.xpath(".//div[@class = 'pricing-row-mobile__name']/text()").get()
            amount_total = item.xpath(".//div[@class = 'pricing-row-mobile__basic-price']/text()").get()
            change_price = item.xpath(".//div[@class = 'pricing-row-mobile__premium-price']/text()").get()
            yield {
                "Title": title,
                "Amount":amount_total,
                "24H Change": change_price

            }
