#! python3
'''
	Get xkcd comixes
'''

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
	#TODO: download the page
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)
	
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		try:
			comicUrl = 'http:' + comicElem[0].get('src')
			print('Downloading image %s...' % (comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			# skip this comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com' + prevLink
			continue
	
	#TODO: save image to ./xkcd
	#TODO: get the Prev button's url
print('Done.')