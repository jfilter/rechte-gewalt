import requests
import dataset
from lxml.html import document_fromstring

import datetime
import re

db = dataset.connect('sqlite:///data.db')

table = db['ST']

base_url = 'http://www.mobile-opferberatung.de/monitoring/chronik%s/'

fix_location = re.compile('\(.*|\/.*')

indices = range(2003, 2017)

for i in indices:

	url = base_url % i

	print('Sending Requests:')
	print(url)

	r = requests.get(url)

	doc = document_fromstring(r.text)

	for entry in doc.xpath('//h5'):

		source_list = entry.xpath('./text()')
		if len(source_list) > 0:
			source = source_list[0]
		else:
			source = 'Unbekannt'

		head = entry.xpath('./following-sibling::h1[1]/text()')[0]

		# add all parts to one large string
		raw_text = ""
		for part in entry.xpath('./following-sibling::div[1]/text()'):
			raw_text += " " + part

		text = re.sub(r"<!--.*-->", "", raw_text).strip()

		head_split = head.split()

		raw_date = head_split[0]
		date = datetime.datetime.strptime(raw_date, '%d.%m.%Y').isoformat()

		# just location
		raw_location = ' '.join(head_split[1:len(head_split)])

		# but sometimes with 'Landkreisen'
		# we want to clean the data and remove them
		location = fix_location.sub('', raw_location)

		# sometimes new white spaces need to be stripped again
		location = location.strip()

		db.begin()
		try:
			table.insert(dict(source=source, text=text, date=date, location=location))
			db.commit()
		except:
			db.rollback()
