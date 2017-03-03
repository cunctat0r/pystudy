#! python3
'''
	Get bash.im comixes
'''

import requests, os, bs4

url = 'http://bash.im/comics'
os.makedirs('bash', exist_ok=True)
while not url.endswith('#'):
	#TODO: download the page
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)
	
	comicElem = soup.select('#the_strip img ')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		try:
			comicUrl = comicElem[0].get('src')
			print('Downloading image %s...' % (comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			# skip this comic			
			prevLink = soup.select('#navi  div.thumbs span')[1]			
			prevLink = prevLink.select('a')[0]
			url = 'http://bash.im' + prevLink.get('href')
			continue
	
	#save image to ./xkcd
	imageFile = open(os.path.join('bash', os.path.basename(comicUrl)), 'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()
	#get the Prev button's url
	#prevLink = soup.select('a[rel="prev"]')[0]
	prevLink = soup.select('#navi  div.thumbs span')[1]			
	prevLink = prevLink.select('a')[0]
	url = 'http://bash.im' + prevLink.get('href')
print('Done.')