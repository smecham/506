# Winter 2018
# SI 506 - Programming I
# Section 9 - 3/13

import requests
import json

# Step 1
baseurl = 'https://itunes.apple.com/search'
dp = {}
dp['term'] = 'The Beatles'
dp['entity'] = 'song'

resp = requests.get(baseurl,params=dp)
#print(resp.status_code)
#print(resp.text)

python_obj = json.loads(resp.text)

# Step 2
#print(json.dumps(python_obj, indent=2))

# Step 3
def get_from_itunes(name, mtype='song', m=50):
	baseurl2 = 'https://itunes.apple.com/search'
	dp2 = {}
	dp2['term'] = name
	dp2['entity'] = mtype
	dp2['limit'] = m
	resp2 = requests.get(baseurl2,params=dp2)
	resp2 = resp2.text
	python_obj2 = json.loads(resp2)
	return python_obj2

# Step 4
#print(type(get_from_itunes('Jackson')))
#print(get_from_itunes('Jackson'))

# Step 5
def get_titles(name, mtype='song', m=50):
	d = get_from_itunes(name, mtype, m)
	#return len(d['results'])
	lst = []
	for item in d['results']:
		lst.append(item['trackName'])
	return lst

print(get_titles('Sun'))