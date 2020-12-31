import scrapy


class P2pSpider(scrapy.Spider):
    name = 'p2p'
    allowed_domains = ['p2p.org']
    start_urls = ['https://p2p.org/']
    #custom_settings = {
        #'FEED_FORMAT':'json',
        #'FEED_URI':'new.json'
    #}
    

    def parse(self, response):
        items = response.xpath(
            "//div[@class = 'NetworkCard__Wrapper-sc-1jic9d2-10 jsnyzI']")
        for item in items:
            title = item.xpath(
                ".//h3[@class = 'NetworkCard__Name-sc-1jic9d2-3 eNboZA']/text()").get()
            value = item.xpath(
                ".//p[@class = 'NetworkCard__Percent-sc-1jic9d2-7 hZhEkZ']/text()").getall()
            final_value = ''.join(value)
            yield {
                "Title": title,
                "Value": final_value
            }
