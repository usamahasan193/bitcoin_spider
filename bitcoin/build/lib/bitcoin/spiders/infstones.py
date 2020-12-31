import scrapy
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from selenium import webdriver
from shutil import which
import time

class InfstonesSpider(scrapy.Spider):
    name = 'infstones'
    allowed_domains = ['infinitystones.io']
    start_urls = ['https://infinitystones.io/staking/']
    

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_path = which("chromedriver")
        driver = webdriver.Chrome(
            executable_path=chrome_path, options=chrome_options)
        driver.get("https://infinitystones.io/staking/")
        time.sleep(3)
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        items = resp.xpath("//div[@class = 'ant-row list-row']")
        for item in items:
            title = item.xpath(".//div[@class = 'ant-col']/text()").getall()
            stacking_ratio = item.xpath(".//div[@class = 'ant-col align-right']/text()").getall()
            yield {
                "Title": title[0],
                "Price": title[1],
                "Annual ROI": stacking_ratio[0],
                "Stacking Ratio": stacking_ratio[1],
                "Market Cap": stacking_ratio[2]
            }

        
        
