import dataset

db = dataset.connect('sqlite:///data.db')

table = db['ST']

db.begin()
try:
	for row in table.all():

		loc = row['location']

		if loc == 'Wolfen-Bitterfeld' or  loc == 'Wolfen' or loc == 'Bitterfeld':
			row['location'] = 'Bitterfeld-Wolfen'

		if loc == 'Dessau' or  loc == 'Dessau Roßlau' or loc == 'Dessau-Rosslau':
			row['location'] = 'Dessau-Roßlau'

		if loc == 'Eilsleben':
			row['location'] = 'Eisleben'

		if loc == 'Laucha an der Unstrut':
			row['location'] = 'Laucha'

		if loc == 'Regionalbahn bei Calbe':
			row['location'] = 'Calbe'

		# if row was manipulated
		if row['location'] != loc:
			print('updating!')
			table.update(row, ['id'])

		# incident happend in train
		# remove it
		if loc == 'Landkreis Anhalt-Zerbst':
			table.delete(id=row['id'])

	db.commit()
except:
	db.rollback()