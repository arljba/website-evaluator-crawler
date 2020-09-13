import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from ..items import WebCheckScraperItem


class LinkSpider(CrawlSpider):
    # The name of the spider
    name = "linkspider"

    # responses that should be handeld
    handle_httpstatus_list = [404, 410, 500]

    # amount of pages that are being crawled. Keep it low to be considerate its just as a proof of concept.
    COUNT_MAX = 50
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': COUNT_MAX
    }

    # scrapyrt (the webserver) doesnt allow params like domain ur starturl to be passed. Therefor this is a hacky way to extract params from the url.
    # this fix follows the instructions given in (https://github.com/scrapinghub/scrapyrt/issues/29)
    __allowedDomain = ("domain")
    __allowedUrls = ("starturl")
    domain = None
    starturl = None

    def __init__(self, domain=None, starturl=None, * args, **kwargs):
        super(LinkSpider, self).__init__(*args, **kwargs)
        for k, v in kwargs.items():
            assert(k in self.__class__.__allowedDomain)
            setattr(self, k, v)
            assert(k in self.__class__.__allowedUrls)
            setattr(self, k, v)
        self.allowed_domains = [domain]
        self.start_urls = [starturl]
        print(self.allowed_domains)
        print(self.start_urls)

    rules = [
        Rule(
            LinkExtractor(
                unique=True
            ),
            follow=True,  # recursive call
            callback="parse_items"
        ),
    ]

    # Method for parsing items

    def parse_items(self, response):
        item = WebCheckScraperItem()
        item['url_src'] = response.request.headers.get('Referer').decode()
        item['url_dest'] = response.url
        item['status'] = response.status
        yield item
