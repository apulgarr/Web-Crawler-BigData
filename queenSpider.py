from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from multiprocessing import Process, Lock
import csv
#from urllib.request import urlopen
from urllib2 import urlopen #in python 2
#import time
import sys


headersToLink = dict()
allFilesNames = set()
mutex = Lock()
#this method will take the  name of csv file without numbers 
def getJustName(filename):
    name = ""
    for i in filename:
        if(i.isdigit()):
            break
        name += i
        
    return name


class MySpider(CrawlSpider):
    name = "queenSpider"
    allowed_domains = ["siata.gov.co"]
    start_urls = ["https://siata.gov.co/descarga_siata/////////application/assets/assets-siata/downloads/"]
    
    rules = (
        Rule(LinkExtractor(allow=r'https://siata.gov.co/descarga_siata/////////application/assets/assets-siata/downloads/\w+'),callback="parse_items", follow= True),
        #Rule(LinkExtractor(allow=(), restrict_xpaths=('//pre',)), callback="parse_items", follow= True),
    )


    def parse_items(self, response):
        if(response.url.endswith(".csv")):
            url = response.url
            fileName = url.split("/")[-1]
            key = getJustName(fileName)
            
            if key in headersToLink:
                if(not fileName in allFilesNames):
                    headersToLink[key].write(url+"\n")
                    allFilesNames.add(str(fileName))
                
            else:
                line =  urlopen(url).readline()
                f = open( "linksFolder/"+key+".txt","a")
                f.write(line)                
                f.write(url+"\n")
                headersToLink[key] = f
                allFilesNames.add(fileName)