import json
import requests

##### START OF CACHE-SPECIFIC FUNCTIONS

CACHE_FILENAME = 'itunes_cache.json'
CACHE = None

def load_cache_from_file():
	global CACHE
	try:
		f = open(CACHE_FILENAME, 'r')
		CACHE = json.loads(f.read())
		f.close()
		print('Loaded cache from', CACHE_FILENAME)
	except:
		# Cache file does not exist, initialize an empty cache
		CACHE = {}
		save_cache_to_file()

def save_cache_to_file():
	if CACHE is not None:
		f = open(CACHE_FILENAME, 'w')
		f.write(json.dumps(CACHE))
		f.close()
		print('Saved cache to', CACHE_FILENAME)

def construct_cache_key(name, mtype):
	return '#'.join(name.split()) + '_' + mtype

### END OF CACHE-SPECIFIC FUNCTIONS


def get_from_itunes(name, mtype="song"):
	request_key = construct_cache_key(name, mtype)
	if request_key in CACHE:
		# The response is already present in our cache
		return CACHE[request_key]

	baseurl = "https://itunes.apple.com/search"
	parameters = {}
	parameters["term"] = name
	parameters["entity"] = mtype
	print("Making request to iTunes API...")
	response = requests.get(baseurl, params=parameters)
	python_obj = json.loads(response.text)
	final_list = []
	for item in python_obj["results"]: 
		final_list.append(item["trackName"])

	# Cache this response and save the cache to file
	CACHE[request_key] = final_list
	save_cache_to_file()

	return final_list

#### MAIN SCOPE

load_cache_from_file()
flag = True
while flag:
	name = input('Enter an artist or band name: ')
	if name.strip().lower() == 'quit':
		flag = False
		break
	mtype = input('Enter a media type (song or musicVideo): ')

	song_list = get_from_itunes(name, mtype)
	print(song_list)
