usage: Animeget [-h] [-u] [-d] [-n USERNAME] [-b] [-m MAL] [-c] [--version]

Use BakaUpdates to fetch new anime releases and integrates with myanimelist to show 
you new releases of what you are currently watching

Program Written By: Christian Nicholson - Cosmos-world.com

optional arguments:
  -h, --help            show this help message and exit
  -u, --update          Only get updates of new releases but do not display
                        them
  -d, --display         Do not download new lists just display new releases
                        for anime in your list
  -n USERNAME, --username USERNAME
                        Use this option and supply it with your Myanimelist
                        username to compare your currently watching to the
                        list of new releases
  -b, --bakaonly        Download and display new releases from Bakaupdates but
                        do not check your MAL list
  -m MAL, --mal MAL     Supply this with your MAL username and it will only
                        update your MAL list it will not display new releases
                        or check for them
  -c, --clear           This option will clear all the entries from the
                        database file, please note this will not delete the
                        file just remove its entries
  --version             show program's version number and exit

Example Usage:
	Show new releases from the last five days: animeget.py -b (default action if no options supplied)
	Show new releases from your MAL list: animeget.py -n=<your username here>
