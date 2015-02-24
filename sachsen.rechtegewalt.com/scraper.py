import requests
import dataset
from lxml.html import document_fromstring

import datetime
import re

db = dataset.connect('sqlite:///data.db')

table = db['SN']


def process_page(text):
	doc = document_fromstring(text)

	for entry in doc.xpath('//h1'):

		text_list = entry.xpath("./..//p/text()")

		if len(text_list) > 0:
			text = ' '.join(text_list)

			date = entry.xpath('.//time[1]/@datetime')[0]

			location = entry.xpath('./a[1]/@title')[0]

			whole_h1 = ' '.join(entry.xpath('.//text()'))

			if 'Stadt Leipzig' in whole_h1:
				location = 'Leipzig'

			if 'Stadt Dresden' in whole_h1:
				location = 'Dresden'

			if 'Stadt Chemnitz' in whole_h1:
				location = 'Chemnitz'

			source_list = entry.xpath("./..//p[@style='text-align: right;']//text()")
			if len(source_list) > 0:
				source = source_list[0]
			else:
				source = 'Unbekannt'

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
		else:
			print('Not found')	


single_url = 'http://www.raa-sachsen.de/index.php/chronik-gesamt.html'
base_url = 'http://www.raa-sachsen.de/index.php/chronik-gesamt.html?page_n13=%s'

urls = [single_url] + [base_url % i for i in range(2, 379)]
# urls = [single_url]

for url in urls:
	process_page(requests.get(url).text)




	