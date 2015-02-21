import dataset
import json

db = dataset.connect('sqlite:///data.db')

result = db.query('SELECT location, COUNT(*), lat, lng FROM ST GROUP BY location').all()

print(result)

with open('cities.json', 'w') as fp:
    json.dump(result, fp)