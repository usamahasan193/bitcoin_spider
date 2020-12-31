from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
setting = get_project_settings()
process = CrawlerProcess(setting)
for spider_name in process.spiders.list():
    process.crawl(spider_name)
process.start()