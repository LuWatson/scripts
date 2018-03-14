import urllib2
from bs4 import BeautifulSoup

downloaded_data  = urllib2.urlopen('https://www.sweetmarias.com/category/green-coffee#')


soup = BeautifulSoup(downloaded_data, "html.parser")
datum=str(soup.find_all('h3'))
beandex=datum.count("green-coffee-name")
beanname="nothing"


for i in range(beandex):
	start = datum.find('h3 class="green-coffee-name" data-value="') + 41
	end = datum.find('"><a href="/product', start)
	beanname=datum[start:end]
	print(beanname)
	bean_location=datum.find(beanname)
	datum=datum[bean_location:]
