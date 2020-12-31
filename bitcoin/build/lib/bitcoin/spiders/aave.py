import scrapy
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from selenium import webdriver
from shutil import which
import time


class AaveSpider(scrapy.Spider):
    name = 'aave'
    allowed_domains = ['aave.com']
    start_urls = ['https://aave.com/']
  
    

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriver")
        driver = webdriver.Chrome(
            executable_path=chrome_path, options=chrome_options)
        driver.get("https://aave.com/")
        driver.maximize_window()
        time.sleep(25)
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)

        items = resp.xpath("//div[@class = 'TableItem']")
        for item in items:
            title = item.xpath(
                ".//div[@class = 'TokenIcon TableItem__token']/p/text()").get()
            market_size = item.xpath(
                ".//div[@class = 'Value TableItem__value']/p/text()").getall()
            Deposit_apt = item.xpath(
                ".//p[@class = 'APRValue APRValue__orange']/text()").get()
            variable_borrow = item.xpath(
                ".//p[@class =  'APRValue APRValue__secondary']/text()").get()
            stable_borrow = item.xpath(
                ".//p[@class = 'APRValue APRValue__undefined']/text()").get()
            if (len(market_size) < 2):
                market_size.append("")
            yield {
                "Title": title,
                "Market Size": market_size[0],
                "Total Borrow": market_size[1],
                "Deposit APT": Deposit_apt,
                "Variable Borrow APR": variable_borrow,
                "Stable Borrow APR": stable_borrow

            }
