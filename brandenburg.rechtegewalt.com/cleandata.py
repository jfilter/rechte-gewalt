import dataset

db = dataset.connect('sqlite:///data.db')

table = db['t']

db.begin()
try:
	for row in table.all():

		loc = row['location']

		if loc == 'Werder':
			row['location'] = 'Werder (Havel)'

		if loc == 'Schwedt':
			row['location'] = 'Schwedt/Oder'

		if loc == 'Lübben':
			row['location'] = 'Lübben (Spreewald)'

		if loc == 'Lübbenau/Spreewald':
			row['location'] = 'Lübben (Spreewald)'

		if loc == 'Lübbenau':
			row['location'] = 'Lübbenau/Spreewald'

		if loc == 'Bad Freienwalde':
			row['location'] = 'Bad Freienwalde (Oder)'

		if loc == 'Bernau':
			row['location'] = 'Bernau bei Berlin'

		if loc == 'Blankenfelde':
			row['location'] = 'Blankenfelde-Mahlow'

		if loc == 'Mahlow':
			row['location'] = 'Blankenfelde-Mahlow'

		if loc == 'Mahlow-Blankenfelde':
			row['location'] = 'Blankenfelde-Mahlow'

		if loc == 'Dahlewitz':
			row['location'] = 'Blankenfelde-Mahlow'

		if loc == 'Brandenburg/Havel':
			row['location'] = 'Brandenburg an der Havel'

		if loc == 'Frankfurt/Oder':
			row['location'] = 'Frankfurt (Oder)'

		if loc == 'Zepernick':
			row['location'] = 'Panketal'

		if loc == 'Schenkendorf':
			row['location'] = 'Steinreich'

		if loc == 'Waltstadt':
			row['location'] = 'Zossen'

		if loc == 'Niederlehme':
			row['location'] = 'Königs Wusterhausen'

		if loc == 'Fürstenwalde':
			row['location'] = 'Fürstenwalde/Spree'

		if loc == 'Joachimsthal (Schorfheide)':
			row['location'] = 'Joachimsthal'

		if loc == 'Schönwalde':
			row['location'] = 'Schönwalde-Glien'

		if loc == 'Falkenberg':
			row['location'] = 'Falkenberg/Elster'

		if loc == 'Bad Belzig':
			row['location'] = 'Belzig'

		if loc == 'Prenzlau – Dedelow':
			row['location'] = 'Prenzlau'

		if loc == 'Ortsteil Dedelow':
			row['location'] = 'Prenzlau'

		if loc == 'Potsdam-Fahrland':
			row['location'] = 'Potsdam'

		if loc == 'Neuenhagen bei Berlin':
			row['location'] = 'Neuenhagen'

		if loc == 'Velten, OT Bärenklau':
			row['location'] = 'Velten'

		if loc == 'Templin/OT Annenwalde':
			row['location'] = 'Templin'

		if loc == 'Schönwald-Glien':
			row['location'] = 'Schönwalde-Glien'

		if loc == 'Brandenburg':
			row['location'] = 'Brandenburg an der Havel'

		if loc == 'Beelitz-Heilstätten':
			row['location'] = 'Beelitz'

		if loc == 'Borgsdorf-Pinnow':
			row['location'] = 'Borgsdorf'

		if loc == 'Dahlwitz-Hoppegarten':
			row['location'] = 'Dahlwitz'

		if loc == 'Flieth':
			row['location'] = 'Flieth-Stegelitz'

		if loc == 'Wittstock/Dosse':
			row['location'] = 'Wittstock'

		if loc == 'Fredersdorf':
			row['location'] = 'Fredersdorf-Vogelsdorf'

		if loc == 'Frehne, Meyenburg':
			row['location'] = 'Marienfließ'

		if loc == 'Sedlitz':
			row['location'] = 'Senftenberg'

		if loc == 'Niedergörsdorf, OT Altes Lager':
			row['location'] = 'Niedergörsdorf'

		if loc == 'Bergholz-Rehbrücke':
			row['location'] = 'Nuthetal'

		if loc == 'Massen':
			row['location'] = 'Massen-Niederlausitz'

		if loc == 'Göttlin':
			row['location'] = 'Rathenow'

		if loc == 'Mögelin':
			row['location'] = 'Premnitz'

		if loc == 'Linumer Bruch':
			row['location'] = 'Neuruppin'

		if loc == 'Lehnitz':
			row['location'] = 'Oranienburg'

		if loc == 'Dahlwitz':
			row['location'] = 'Hoppegarten'

		if loc == 'Neu Fahrland':
			row['location'] = 'Potsdam'

		if loc == 'Am Schlaatz':
			row['location'] = 'Potsdam'

		if loc == 'Pirschheide':
			row['location'] = 'Potsdam'

		if loc == 'Bornstedt':
			row['location'] = 'Potsdam'

		if loc == 'Drewitz':
			row['location'] = 'Potsdam'

		if loc == 'Neu Lübbenau':
			row['location'] = 'Unterspreewald'

		if loc == 'Leibsch':
			row['location'] = 'Unterspreewald'
	
		if loc == 'Körba':
			row['location'] = 'Lebusa'

		if loc == 'Freileben':
			row['location'] = 'Lebusa'



		# if row was manipulated
		if row['location'] != loc:
			print('updating!')
			table.update(row, ['id'])

		# incident happend in train
		# remove it
		if loc == 'Zug Wien-Hamburg':
			table.delete(id=row['id'])

		# incident happend in bus
		if loc == 'Sedlitz/Großräschen':
			table.delete(id=row['id'])

	db.commit()
except:
	db.rollback()