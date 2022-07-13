import re
import scrapy

from pep_parse.items import PepParseItem
from urllib.parse import urljoin

NEEDED_URL = 0


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps = response.xpath(
            '//section[@id="numerical-index"]//tbody//tr')
        for pep_url in peps:
            pep = urljoin(PepSpider.start_urls[NEEDED_URL],
                          pep_url.css('td a::attr(href)').get())
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.xpath('//h1[@class="page-title"]/text()').get()
        number = re.search(r'^PEP (?P<number>\d+)', title).group('number')
        status = response.xpath(
            '//dt[contains(.,"Status")]/following-sibling::dd/text()'
        ).get()

        data = {
            'number': number,
            'name': title,
            'status': status,
        }
        yield PepParseItem(data)
