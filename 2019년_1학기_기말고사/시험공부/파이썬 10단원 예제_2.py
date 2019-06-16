#크롤링
n_crawler = NaverCrawler()
d_crawler = DaumCrawler()
crawlers = [n_crawler,d_crawler]
news = []
for crawler in crawlers:
    news.append(crawler.do_crawing())
