#! python3
'''
	Get xkcd comixes
'''

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
	#TODO: download the page
	#TODO: find the url of image
	#TODO: download the image
	#TODO: save image to ./xkcd
	#TODO: get the Prev button's url
print('Done.')