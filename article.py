# Creating web spider scraper for few links in wikipedia using Scrapy

# Creating Venv scrapy_venv_v2 , using Anaconda
# Install Scrapy Framework , using Anaconda
# Prepare Scrapy framework, $ scrapy startproject wikiSpider_v2 . 
# New folder created "wikispider_v2".
# Folder contains some files and subfoders created for scrapy project.
# creat new file article.py in this location wikiSpider_v2/wikiSpider_v2/spiders/article.py
# article.py:
    
# import scrapy Lib
import scrapy


# this class is responsible to scrap only under article pages
class ArticleSpider(scrapy.Spider):
    name = 'article'
# we define two two functions 1 for requists and 1 for feedback
    def start_requests(self):
        # Input 3 URL to be scraped
        urls = [
                'http://en.wikipedia.org/wiki/Python_%28programming_language%29',
                'https://en.wikipedia.org/wiki/Functional_programming',
                'https://en.wikipedia.org/wiki/Monty_Python']
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]
    
    def parse(self, response):
        
        url =  response.url
        title  = response.css('h1::text').extract_first()
        
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))
        
        
# We run in terminal in side the fo;der of article.py :
# scrapy runspider article.py
# URL is: https://en.wikipedia.org/wiki/Functional_programming
#Title is: Functional programming
# 2022-07-06 09:23:07 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://en.wikipedia.org/wiki/Monty_Python> (referer: None)
# 2022-07-06 09:23:07 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://en.wikipedia.org/wiki/Python_%28programming_language%29> (referer: None)
# URL is: https://en.wikipedia.org/wiki/Monty_Python
# Title is: Monty Python
# URL is: https://en.wikipedia.org/wiki/Python_%28programming_language%29
# Title is: Python (programming language)
# 2022-07-06 09:23:07 [scrapy.core.engine] INFO: Closing spider (finished)
#The scraper goes to the three pages listed as the start_urls, gathers information, and then terminates.