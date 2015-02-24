import dataset
import requests
import time

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s'

db = dataset.connect('sqlite:///data.db')

table = db['ST']

results = []
for row in table.distinct('location'):

	print(row)

	loc = row['location']
	adress = loc + ',Sachsen-Anhalt'
	url = base_url % adress

	try:
		r = requests.get(url)
		json_data = r.json()
		geolocation = json_data['results'][0]['geometry']['location']
	except Exception as e:
		print(e)

	print(geolocation)

	results += [dict(lng=geolocation['lng'], lat=geolocation['lat'], location=loc)]
	time.sleep(0.5)

# now save it in db
db.begin()
try:
	for r in results:
		table.update(r, ['location'])

	db.commit()
except Exception as ee:
	print(ee)
	db.rollback()