import dataset

db = dataset.connect('sqlite:///data.db')

table = db['SN']

db.begin()
try:
	for row in table.all():

		loc = row['location']

		if loc == 'Angetrunkene Jugendliche zeigen Hitlergruß':
			row['location'] = 'Stolpen'

		if loc == 'Angriff auf 45- jährigen':
			row['location'] = 'Zwickau'

		if loc == 'Angriff auf Wohnhaus':
			row['location'] = 'Geringswalde'

		if loc == 'Nazirandale in Colditz':
			row['location'] = 'Colditz'

		# interpolating from text, happens often, so maybe Görlitz?
		if loc == 'Angriff auf alternatives Hausprojekt':
			row['location'] = 'Görlitz'

		if loc == 'Angriffe auf Jugendtreff und Coffee Shop':
			row['location'] = 'Rochlitz'

		if loc == 'Belästigung und Einschüchterung':
			row['location'] = 'Rochlitz'

		if loc == 'Annaberg Buchholz':
			row['location'] = 'Annaberg-Buchholz'

		if loc == 'Bon Courage fassungslos über Naziübergriffe auf dem Bornaer Stadtfest':
			row['location'] = 'Borna'

		if loc == 'Borna: Mahnmal für KZ-Opfer mit antisemitischer Parole besprüht':
			row['location'] = 'Borna'

		if loc == 'Brand- Erbisdorf':
			row['location'] = 'Brand-Erbisdorf'

		if loc == 'Brand-Erbisdorf/ Gränitz':
			row['location'] = 'Brand-Erbisdorf'

		if loc == 'Eilenbrurg':
			row['location'] = 'Eilenburg'

		if loc == 'Eilenburg, Oschatz':
			row['location'] = 'Eilenburg'

		if loc == 'Zwönitz OT Kühnheide':
			row['location'] = 'Zwönitz'

		if loc == 'Zwickau Hauptmarkt':
			row['location'] = 'Zwickau'

		if loc == 'Zschoppach/Nauberg':
			row['location'] = 'Zschopau'

		if loc == 'Zschepplin/Hohenprießnitz':
			row['location'] = 'Zschepplin'

		if loc == 'Zschadraß (OT Zollwitz)':
			row['location'] = 'Zschadraß'

		if loc == 'Wurzen/Bennewitz':
			row['location'] = 'Wurzen'

		# uncertain
		if loc == 'Verfassungsfeindliche Symbole':
			row['location'] = 'Penig'

		if loc == 'Verfassungsfeindliche Schmierereien':
			row['location'] = 'Schwarzenberg'

		if loc == 'Stauchitz OT Seerhausen':
			row['location'] = 'Stauchitz'

		if loc == 'Stiebitz (Bautzen)':
			row['location'] = 'Bautzen'

		if loc == 'NPD organisiert neonazistisches Fußballturnier bei Oschatz':
			row['location'] = 'Naundorf'

		if loc == 'Stadt Zwickau':
			row['location'] = 'Zwickau'

		if loc == 'Neonazi als Security bei Schwetaer Parkfest':
			row['location'] = 'Mügeln'

		if loc == 'Schweta':
			row['location'] = 'Mügeln'

		if loc == 'Neonazis auf dem Spielplatz':
			row['location'] = 'Mittweida'

		if loc == 'Riesa - Großenhain':
			row['location'] = 'Riesa'

		if loc == 'Panschwitz Kuckau, OT Ostro':
			row['location'] = 'Panschwitz-Kuckau'

		# check street
		if loc == 'Paulsdorf, Talsperrenstraße':
			row['location'] = 'Dippoldiswalde'

		#  Beilrode Gemeinde Mergin...
		if loc == 'Zwethau':
			row['location'] = 'Beilrode'


		#  Weischlitz Gemeinde Mergin...
		if loc == 'Burgstein, OT Gutenfürst':
			row['location'] = 'Weischlitz'


		if loc == 'Torgau OT Staupitz':
			row['location'] = 'Torgau'

		if loc == 'Taucha/Dresden':
			row['location'] = 'Taucha'

		if loc == 'Langburkersdorf':
			row['location'] = 'Neustadt'

		if loc == 'Sebitz':
			row['location'] = 'Sebnitz'

		if loc == 'Reichenbach/OL':
			row['location'] = 'Reichenbach'

		if loc == 'Pirna Rottwerndorf':
			row['location'] = 'Pirna'

		if loc == 'OT Neuplanitz':
			row['location'] = 'Zwickau'

		if loc == 'Treuen bei Plauen':
			row['location'] = 'Treuen'

		if loc == 'Oelsnitz/E.':
			row['location'] = 'Oelsnitz'

		if loc == 'Mügeln/Niedergoseln':
			row['location'] = 'Mügeln'

		if loc == 'Liegau-Augustusbad':
			row['location'] = 'Radeberg'

		if loc == 'Gröditz, OT Spansberg':
			row['location'] = 'Gröditz'

		if loc == 'Schönwölkau/Badrina':
			row['location'] = 'Schönwölkau'

		if loc == 'Schloss Nöthnitz / Bannewitz':
			row['location'] = 'Bannewitz'

		if loc == 'Markleeberg':
			row['location'] = 'Markkleeberg'

		if loc == 'Lommatszch':
			row['location'] = 'Lommatzsch'

		if loc == 'Lohsa - OT Groß Särchen':
			row['location'] = 'Lohsa'

		if loc == 'Leißnig':
			row['location'] = 'Leisnig'

		if loc == 'Grimma OT Roda':
			row['location'] = 'Grimma'

		if loc == 'Wedelwitz':
			row['location'] = 'Eilenburg'

		if loc == 'Annaberg':
			row['location'] = 'Annaberg-Buchholz'

		if loc == 'Bautzen-Gesundbrunnen':
			row['location'] = 'Bautzen'

		if loc == 'Mutzschen (OT Roda)':
			row['location'] = 'Mutzschen'

		if loc == 'Krostitz, OT Lehelitz':
			row['location'] = 'Krostitz'

		if loc == '':
			row['location'] = 'Geithain'

		if loc == '(Geithain)':
			row['location'] = 'Geithain'

		if loc == 'Togau':
			row['location'] = 'Torgau'

		if loc == 'Zschadraß':
			row['location'] = 'Colditz'

		if loc == 'Rosswein':
			row['location'] = 'Roßwein'

		if loc == 'Oelsa/Rabenau':
			row['location'] = 'Rabenau'

		if loc == 'Doberschütz OT Sprotta-Siedlung':
			row['location'] = 'Doberschütz'

		if loc == 'Meissen':
			row['location'] = 'Meißen'

		if loc == 'Neonazistische Parolen vor Supermarkt in Wurzen':
			row['location'] = 'Wurzen'

		if loc == 'Ralbitz-Rosenthal OT Ralbitz' or loc == 'Ralbitz-Rosenthal OT Schönau':
			row['location'] = 'Ralbitz-Rosenthal'

		if loc == 'Laußig/Authausen' or loc == 'Laußig/Pressel':
			row['location'] = 'Laußig'


		if loc == 'Roter Stern Gastspiel in Schildau: Polizei nimmt Neonazis fest':
			row['location'] = 'Schildau'

		if loc == 'Rußdorf bei Limbach-Oberfrohna':
			row['location'] = 'Limbach-Oberfrohna'

		if loc == 'Kändler, bei Limbach Oberfrohna':
			row['location'] = 'Limbach-Oberfrohna'


		if loc == 'Limbach' or loc == 'Limbach - Oberfrohna' or loc == 'Limbach Oberfrohna' or loc == 'Limbach- Oberfrohna' or loc == 'Limbach-Oberfohnah':
			row['location'] = 'Limbach-Oberfrohna'

		if loc == 'Neustadt i. Sa.' or loc == 'Neustadt i. Sa. - Langburkersdorf' or loc == 'Neustadt i.Sa.':
			row['location'] = 'Neustadt'


		# if row was manipulated
		if row['location'] != loc:
			print('updating!')
			table.update(row, ['id'])

		# incident happend in train
		# remove it

		# remove, no real 'incident', no real spot
		if loc == 'Borna/Geithain':
			table.delete(id=row['id'])

		if loc == 'Borna/Döbeln/Eilenburg/Taucha':
			table.delete(id=row['id'])

		if loc == 'Lauter/Schwarzenberg/Breitenbrunn':
			table.delete(id=row['id'])

		if loc == 'Borna/Döbeln/Eilenbrug/Taucha':
			table.delete(id=row['id'])

		if loc == 'Böhla  und Weißig (bei Nünchritz)':
			table.delete(id=row['id'])



		if loc == 'Wurzen/Leipzig':
			table.delete(id=row['id'])

		if loc == 'Markkleeberg/Döbeln':
			table.delete(id=row['id'])

		if loc == 'Döbeln/Leisnig':
			table.delete(id=row['id'])

		if loc == 'Johanngeorgenstadt/Hoyerswerda':
			table.delete(id=row['id'])

		if loc == 'Großröhrsdorf, Steina, Pulsnitz':
			table.delete(id=row['id'])

		if loc == 'Wurzen/Markkleeberg/Döbeln':
			table.delete(id=row['id'])

		# remove, or all?
		if loc == 'Mittweida, Geringswalde, Rochlitz':
			table.delete(id=row['id'])

		# remove, or all?
		if loc == 'Kohren-Salis, Geithain, Borna und Frohburg':
			table.delete(id=row['id'])


		if loc == 'Delitzsch/Eilenburg':
			table.delete(id=row['id'])

		if loc == 'Grimma/Großpösna/Taucha/Beilrode':
			table.delete(id=row['id'])

		if loc == 'Grimma/Döbeln':
			table.delete(id=row['id'])

		if loc == 'Dippoldiswalde/ Freital':
			table.delete(id=row['id'])

		if loc == 'Delitzsch/Eilenburg/Torgau':
			table.delete(id=row['id'])

		if loc == 'CDU fordert Rücktritt vom Chef des Tourismusvereins':
			table.delete(id=row['id'])

		if loc == 'Böhlen/Großdeuben':
			table.delete(id=row['id'])

		if loc == 'LK Nordsachsen':
			table.delete(id=row['id'])

		if loc == 'Angriffe auf Bürgerbüros':
			table.delete(id=row['id'])

		if loc == 'Sächsische Schweiz':
			table.delete(id=row['id'])

		# No location given
		if loc == 'Wahlplakat beschmiert':
			table.delete(id=row['id'])

		# No location given
		if loc == 'Verfolgungsjagd im Auto':
			table.delete(id=row['id'])

		# Train
		if loc == 'Leipzig-Borna':
			table.delete(id=row['id'])

		if loc == 'Deutsche Bahn':
			table.delete(id=row['id'])

		if loc == 'A4':
			table.delete(id=row['id'])

	db.commit()
except:
	db.rollback()