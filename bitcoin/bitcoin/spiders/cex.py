import scrapy


class CexSpider(scrapy.Spider):
    name = 'cex'
    allowed_domains = ['staking.cex.io']
    start_urls = ['https://staking.cex.io/']
    
    
    def parse(self, response):
        title_list = []
        my_estimate = []
        my_minimum  = []
        my_maximum = []
        title = response.xpath(
            "//div[@class = 'subtitle']//span/text()").getall()
        estimated_annual_yeild = response.xpath(
            "//span[@class = 'coin-text coin-rate']/text()").getall()
        minimum_holding = response.xpath(
            "//span[@class = 'coin-text']/text()").getall()
        del title[0]
        del title[1]
        for i in range(0, len(title)):
            new_title = (title[i])
            estimated_yield = (estimated_annual_yeild[i])
            title_list.append(new_title)
            my_estimate.append(estimated_yield)

        for l in range(0, len(minimum_holding)):
            if(l%2==0):
                minimum = (minimum_holding[l])
                my_minimum.append(minimum)
        for m in range(0, len(minimum_holding)):
            if(m%2!=0):
                maximum = (minimum_holding[m])
                my_maximum.append(maximum)
        for o in range(0,len(title_list)):
            yield{
                "Title": title_list[o],
                "Estimated Annual Yield": my_estimate[o],
                "Minimum Holding": my_minimum[o],
                "Reward Coin": my_maximum[o]
            }
                
          
