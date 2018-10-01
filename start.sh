rm -r linksFolder
rm -r generatedSpiders
rm -r generatedData
mkdir linksFolder
mkdir generatedSpiders
mkdir generatedData
if [$1 = "nohup" ]; then    
    nohup python2 -m scrapy runspider queenSpider.py -s LOG_ENABLED=False &
else
    python2 -m scrapy runspider queenSpider.py -s LOG_ENABLED=False
fi
python2 spiderGenerator.py

