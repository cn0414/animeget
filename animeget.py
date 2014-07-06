import urllib2 #library to fetch html code
import BeautifulSoup #library to parse html code
import sqlite3 #library to interact with sqlite database
import argparse #library for command line interfaces
import textwrap #library for use with parseing and argparser for textwraping
from datetime import datetime #library for getting date and time



date = str(datetime.now().date())

conn = sqlite3.connect('anime.db')
c = conn.cursor()


def init():
	
	c.execute('''CREATE TABLE IF NOT EXISTS release
			(date text, animename text, episodenumber integer, subgroup text)''')
	conn.commit()
	
	c.execute('''CREATE TABLE IF NOT EXISTS mylist
			(date text, animename text, episodenumber integer)''')
	conn.commit()

def getrelease():
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

def getmylist(username):
	print 'Still in progress will retrieve list from MAL'
	
def updateonly():
	print 'Still in progress will retrieve updates to lists and update database but not display them'

def onlydisplay():
	print 'Still in progress will display comparison of lists in database to show new releases for your currently watching but will not download new lists'
	
def malrelease(username):
	print 'Still in progress will download currently watching from MAL using supplied username and releases from Bakaupdates store them in the database and compare to print out new releases for your currently watching'
	
def malonly(username):
	print 'Still in progress will download your MAL list only and display nothing'

def emptydb():
	print 'Still in progress will delete all entries in database file but not the file itself'

parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description=textwrap.dedent('''\
	Use BakaUpdates to fetch new anime releases and integrates with myanimelist to show 
	you new releases of what you are currently watching
	
	Program Written By: Christian Nicholson - Cosmos-world.com
	'''),
	prog='Animeget',
	epilog=textwrap.dedent('''\
	Example Usage:
		Show new releases from the last five days: animeget.py -b (default action if no options supplied)
		Show new releases from your MAL list: animeget.py -n=<your username here>
	''')
	)
parser.add_argument(
	'-u', '--update',
	help='Only get updates of new releases but do not display them',
	action='store_true'
	#type=updateonly
	)
parser.add_argument(
	'-d', '--display',
	help='Do not download new lists just display new releases for anime in your list',
	action='store_true'
	#type=onlydisplay
	)
parser.add_argument(
	'-n', '--username',
	help='Use this option and supply it with your Myanimelist username to compare your currently watching to the list of new releases',
	type=malrelease
	)
parser.add_argument(
	'-b', 
	'--bakaonly',
	action='store_true',
	help='Download and display new releases from Bakaupdates but do not check your MAL list'
	# type=getrelease
	)
parser.add_argument(
	'-m', '--mal',
	help='Supply this with your MAL username and it will only update your MAL list it will not display new releases or check for them',
	type=malonly
	)
parser.add_argument(
	'-c', '--clear',
	help='This option will clear all the entries from the database file, please note this will not delete the file just remove its entries',
	action='store_true'
	#type=emptydb
	)

parser.add_argument('--version', action='version', version='%(prog)s .1a')

args = parser.parse_args()

if args.bakaonly:
	getrelease()
if args.clear:
	emptydb()
if args.display:
	onlydisplay()
if args.update:
	updateonly()
		

#getrelease()
conn.commit()
conn.close()
