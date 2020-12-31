import scrapy
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from selenium import webdriver
from shutil import which
import time


class StackinSpider(scrapy.Spider):
    name = 'stackin'
    allowed_domains = ['stakin.com']
    start_urls = ['https://stakin.com/home/']
   

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_path = which("chromedriver")
        driver = webdriver.Chrome(
            executable_path=chrome_path,  options=chrome_options)
        driver.get("https://stakin.com/home/")
        time.sleep(5)
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        items = resp.xpath("//div[@class = 'st-card']")
        for item in items:
            title = item.xpath(".//div[@class = 'st-card__title']/text()").get()
            value = item.xpath(".//div[@class = 'st-card__apr']/text()").get()
            yield {
                "Title": title,
                "Value": value
            }
