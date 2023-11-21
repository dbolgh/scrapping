import scrapy


class TwitterspiderSpider(scrapy.Spider):
    name = "twitterspider"
    allowed_domains = ["twitter.com"]
    start_urls = ["https://twitter.com"]

    def parse(self, response):
        pass
