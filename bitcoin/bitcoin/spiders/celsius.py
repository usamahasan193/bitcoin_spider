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


class CelsiusSpider(scrapy.Spider):
    name = 'celsius'
    allowed_domains = ['celsius.network/']
    start_urls = ['http://celsius.network/earn-rewards-on-your-crypto/#rate_chart/']
    

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriver")
        driver = webdriver.Chrome(
            executable_path=chrome_path, options=chrome_options)
        driver.get("http://celsius.network/earn-rewards-on-your-crypto/#rate_chart/")
        driver.maximize_window()
        driver.implicitly_wait(990000)
        try:
            myDynamicElement = driver.find_element_by_xpath(
                "//div[@class = 'row']")
            
            print(myDynamicElement)
        finally:
            self.html = driver.page_source
            driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        items = resp.xpath("//div[@class = 'row']")
        for item in items:
            title = item.xpath(".//div[@class = 'image']/text()").get()
            cell_reward = item.xpath(".//div[@class= 'cell highlight']/strong/text()").get()
            in_kind_reward = item.xpath(".//div[@class = 'cell']/text()").get()
            

            yield {
                "Title": title,
                "Cell Reward(APY)": cell_reward,
                "In Kind Reward Rate(APY)": in_kind_reward
            }