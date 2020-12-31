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


class MyconatainerSpider(scrapy.Spider):
    name = 'myconatainer'
    allowed_domains = ['mycointainer.com']
    start_urls = ['https://www.mycointainer.com/assets/']
   

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriver")
        driver = webdriver.Chrome(
            executable_path=chrome_path, options=chrome_options)
        driver.get("https://www.mycointainer.com/assets/")
        driver.maximize_window()
        driver.implicitly_wait(990000)
        try:
            myDynamicElement = driver.find_element_by_xpath(
                "//a[@class = 'assetCard_cardContainer__TdVdt']")
            print(myDynamicElement)
        finally:
            self.html = driver.page_source
            driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        items = resp.xpath(
            "//a[@class = 'assetCard_cardContainer__TdVdt']")
        for item in items:
            title = item.xpath(".//h2/text()").get()
            yearly_return = item.xpath(".//div[@class = 'assetCard_cardYearlyReturnValue__1TtPf']/text()").get()
            reward_fee = item.xpath(".//div[@class = 'assetCard_rewardFeeValue__39gcu']/text()").get()
            yield {
                "Title": title,
                "Yearly Return": yearly_return,
                "Reward Fee": reward_fee
            }
