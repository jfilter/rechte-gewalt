import requests
import dataset
from lxml.html import document_fromstring

import datetime
import re
import locale

locale.setlocale(locale.LC_ALL,'de_De')

db = dataset.connect('sqlite:///data.db')

table = db['31032016']


def process_page(text):
	doc = document_fromstring(text)

	for entry in doc.xpath('//article'):

			source_list = entry.xpath("./header/div[@class='quelle']/span/text()")
			if len(source_list) > 0:
				source = source_list[0]
			else:
				source = 'Unbekannt'

			location = entry.xpath("./header/h1/a/text()")[0]

			date_raw = entry.xpath(".//li[@class='post-date']/span/text()")[1]

			date = datetime.datetime.strptime(date_raw, '%d. %B %Y').isoformat()
			
			text = ' '.join(entry.xpath("./section/p//text()"))

			print(location)
			print(source)
			print(date)
			print(text)


			db.begin()
			try:
				table.insert(dict(source=source.strip(), text=text.strip(), date=date, location=location.strip()))
				db.commit()
			except:
				db.rollback()



base_url = 'http://www.opferperspektive.de/category/rechte-angriffe/chronologie-rechter-angriffe/page/%s'

urls = [base_url % i for i in range(1, 94)]

for url in urls:
	process_page(requests.get(url).text)




	