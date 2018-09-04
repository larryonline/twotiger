# -*- coding: utf-8 -*-
import scrapy


class TwoTigerSpider(scrapy.Spider):
    name = "TwoTiger"
    allowed_domains = ["twotiger.com"]
    start_urls = [
        'https://www.twotiger.com/bond/-1',
    ]

    def parse(self, response):

        for item_url in response.css("div.hotItems div.hotItemsListInfo a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_touzi_page)
        next_page = response.css("div.page > ul > li.right > a ::attr(href)").extract_first()

        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

        #
        # for book_url in response.css("article.product_pod > h3 > a ::attr(href)").extract():
        #    yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)
        #next_page = response.css("li.next > a ::attr(href)").extract_first()
        #if next_page:
        #    yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_touzi_page(self, response):
        item = {};

        nameInfo = response.css("div.nameInfo");
        item["name"] = nameInfo.css("p ::text").extract_first();
        item["discount"] = 1 if nameInfo.css("em.dz").extract_first() else 0;

        item["type"] = response.css("div.projectName em.doubt_no ::text").extract_first();

        volumeInfo = response.css("div.lijitouzi");
        item["volume"] = volumeInfo.css("p.mt25 > span.fr ::text").extract_first();
        item["profit"] = volumeInfo.css("p > span#yjsy ::text").extract_first();

        yield item

    def parse_book_page(self, response):
        pass
        item = {}
        product = response.css("div.product_main")
        item["title"] = product.css("h1 ::text").extract_first()
        item['category'] = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()"
        ).extract_first()
        item['description'] = response.xpath(
            "//div[@id='product_description']/following-sibling::p/text()"
        ).extract_first()
        item['price'] = response.css('p.price_color ::text').extract_first()
        yield item
