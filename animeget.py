import urllib2
import BeautifulSoup
import sqlite3
from datetime import datetime

date = str(datetime.now().date())

conn = sqlite3.connect('anime.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS release
		(date text, animename text, episodenumber integer, subgroup text)''')
conn.commit()

def main():
	url = "http://baka-updates.com/releases"
	data = urllib2.urlopen(url).read()
	bs = BeautifulSoup.BeautifulSoup(data)
	
#	anime = bs.find('div', {'id': 'content'})
#	anime = [s.getText().strip() for s in anime.findAll('tr')]

	""" alternate code """
	anime2 = bs.find('div', {'id': 'content'})
	an = anime2.findAll('tr', {'class': 'rlselement'})
	""" do for each """
	for i in an:
		animename = i.td.nextSibling.nextSibling.a.getText()
		epn = i.td.nextSibling.nextSibling.contents
		epn = [int(s) for s in epn[2].split() if s.isdigit()]
		if len(epn) > 0:
			epn = epn[0]
		else:
			epn = 0
		subgroup = i.td.nextSibling.nextSibling.nextSibling.nextSibling.a.text
		animename = str(animename)
		subgroup = str(subgroup)

		c.execute('''INSERT INTO release(date, animename, episodenumber, subgroup)
				VALUES(?,?,?,?)''', (date, animename, epn, subgroup))
		conn.commit()

		print animename ,epn, subgroup #test code
	""" end do for each """

	""" end alternate code """
#	res = '\n'.join(anime)
#	print res
main()
conn.commit()
conn.close()
