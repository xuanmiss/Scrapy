cd weixin
scrapy crawl weixin -o /info/gaokao.json
cd  ..
cd weibo
scrapy crawl weiboseh -o /info/gaokao.json
cd ..
cd newsbaidu
scrapy crawl newsb -o /info/gaokao.json
cd ..
cd tieba
scrapy crawl tiebac -o /info/gaokao.json
