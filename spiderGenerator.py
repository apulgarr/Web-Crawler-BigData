import os
from multiprocessing import Process, Lock, BoundedSemaphore, cpu_count
import glob

originalCode = ['#DONT MODIFY THIS FILE\n','import scrapy\n', 'from scrapy.spiders import CSVFeedSpider\n', 'from scrapy.item import Item, Field\n', 'def getJustNumber(fileName):\n', '    i = 0\n', '    for lett in fileName:\n', '        if(lett.isdigit()):\n', '            break\n', '        i = i + 1\n', '    return fileName[i:]\n', 'class estructure(Item):\n', '    fileName = scrapy.Field()\n', 'class SiataSpider(CSVFeedSpider):\n', "    name = 'siataSpider'\n", "    allowed_domain = 'siata.gov.co'\n", '#THERE MUST BE THE FILES TO LOAD\n', '    def parse_row(self, response, row):\n', '        item = estructure()\n','        item[\'fileName\'] = getJustNumber(response.url.split("/")[-1])\n', '        yield item']
linksFolder = "linksFolder/"
spidersFolder = "generatedSpiders/"
generatedData = "generatedData/"
def executeSpider (fileName, mutex):
    mutex.acquire()
    os.system("python2 -m scrapy runspider "+spidersFolder+fileName+".py -o "+generatedData+fileName+".csv -t csv -s LOG_ENABLED=False")
    mutex.release()


if __name__ == '__main__':
    
    mutex = BoundedSemaphore(cpu_count()) 
    mutex.acquire()
    for file in glob.glob(linksFolder+"*.txt"):
        fields = ""
        parseHeaders = ""
        for  header in open(file,"r").readline()[:-1].split(","):
            if(header == ''):
                fields += "    fecha_hora = scrapy.Field()\n"
                parseHeaders += "        item['fecha_hora'] = row['']\n"
            else:
                fields += "    "+header +" = scrapy.Field()\n"
                parseHeaders += "        item['"+header+"'] = row['"+header+"']\n"
        auxiliarCode = originalCode
        fileName = file.split('/')[1][:-4]
        auxiliarCode[16] = '    start_urls = [str(line)[:-1] for line in open("'+linksFolder+fileName+'.txt", "r").readlines() if line.endswith(".csv\\n")]\n'
        auxiliarCode = auxiliarCode[:12] + [fields] +  auxiliarCode[12:][:7] +[parseHeaders] + auxiliarCode[12:][7:]
        f= open(spidersFolder+fileName+".py","w") 
        for line in auxiliarCode:
            f.write(line)
        f.close()
        Process(target = executeSpider, args=(fileName, mutex)).start()
    mutex.release()
    os._exit(1)
