import dataset
import json

db = dataset.connect('sqlite:///data.db')

locations = db.query('SELECT location, COUNT(*) as n, lat, lng FROM ST GROUP BY location')

result = []

for location in locations:
	x = {}
	x['location'] = location['location']
	x['lat'] = location['lat']
	x['lng'] = location['lng']
	x['n'] = location['n']
	x['incidents'] = []

	count = 0

	for incident in db['ST'].find(location=location['location'], order_by='date'):

		count += 1

		print(count)

		i = {}

		i['source'] = incident['source']
		i['text'] = incident['text']
		i['date'] = incident['date']

		x['incidents'] += [i]

	result += [x]	

print(result)

with open('cities.json', 'w') as fp:
    json.dump(result, fp)