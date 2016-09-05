# -*- coding: utf-8 -*-


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BeerSmithSpider(CrawlSpider):
    name = "BeerSmith"
    start_urls = ['http://beersmithrecipes.com/toprated/']
    page = 0

    rules = (
        Rule(LinkExtractor(allow=('http://beersmithrecipes.com/toprated/*',))),
        Rule(LinkExtractor(allow=('http://beersmithrecipes.com/viewrecipe/*/*', )), callback='parse_recipe'),
    )

    def parse_recipe(self, response):
        recipe = {}
        name = response.css('#main h2::text').extract_first()
        recipe['name'] = name
        for td in response.css('.r_hdr tr td'):
            kv = td.css('::text').extract()
            if len(kv) == 2:
                recipe[kv[0]] = kv[1]
        ingredients = response.css('.recipes tr td::text').extract()
        ingredients_list = []
        for i in range(0, len(ingredients) - 1, 4):
            amount = ingredients[i]
            name = ingredients[i + 1]
            type = ingredients[i + 2]
            ingredients_list.append({"amount": amount, "name": name, "type": type})
        recipe['ingredients'] = ingredients_list
        return recipe
