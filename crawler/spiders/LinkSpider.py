import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from ..items import WebCheckScraperItem


class LinkSpider(CrawlSpider):
    # The name of the spider
    name = "linkspider"

    # only check internal domain links
    allowed_domains = ["hs-flensburg.de"]
    # entry point
    start_urls = ["http://www.hs-flensburg.de/"]

    COUNT_MAX = 5
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': COUNT_MAX
    }

    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,  # recursive call
            callback="parse_items"
        )
    ]

    def parse(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # Method for parsing items

    def parse_items(self, response):
        # liste of founf links
        items = []
        # only canonical and unique links
        links = LinkExtractor(
            canonicalize=True, unique=True).extract_links(response)
        for link in links:
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    is_allowed = True
            if is_allowed:
                item = WebCheckScraperItem()
                item['url_src'] = response.url
                item['url_dest'] = link.url
                items.append(item)
        return items
