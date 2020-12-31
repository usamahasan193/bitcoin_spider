import scrapy
import json
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which
from scrapy.selector import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CryptoexchangeSpider(scrapy.Spider):
    name = 'cryptoexchange'
    allowed_domains = ['crypto.com']
    start_urls = ['https://crypto.com/exchange/']
    

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriver")
        driver = webdriver.Chrome(
            executable_path=chrome_path, options=chrome_options)
        driver.get("https://crypto.com/exchange/")
        driver.maximize_window()
        driver.implicitly_wait(990000)
        try:
            myDynamicElement = driver.find_element_by_xpath("//li[@class = 'home-tbody-li']")
            
            print(myDynamicElement)
        finally:
            self.html = driver.page_source
            driver.close()
    
    def parse(self, response):
        resp = Selector(text=self.html)
        items = resp.xpath("//li[@class = 'home-tbody-li']")
        for item in items:
            title = item.xpath(".//div[@class = 'coin-pair']/span/text()").get()
            relative_price = item.xpath(".//div[@class = 'relative-price']/text()").get()
            used_price = item.xpath(".//div[@class = 'usd-price']/text()").get()
            change = item.xpath(".//button[@class = 'price-change']/text()").get()
            highdiv = item.xpath(".//div[@class = 'even']/text()").getall()
            combined_list = []
            combined_list.append(relative_price )
            combined_list.append(used_price)
            yield {
                "Title": title,
                "Last_price": combined_list,
                "24H Change": change,
                "24H High": highdiv[0],
                "24H Low": highdiv[1],
                "24H Valume": highdiv[2]
            }