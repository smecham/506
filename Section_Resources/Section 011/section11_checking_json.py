import json
import requests
import webbrowser

# iTunes API documentation
# https://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html 
# User-Defined Classes

# Step 1
#-----------------------
# Create a Song Class

# class name
class Song(object):

	# methods:

	# constructor
	def __init__(self, artist_name, track_title, track_url, is_explicit, track_duration):
		# set attributes
		self.artist_name = artist_name # str
		self.track_title = track_title # str
		self.track_url =  track_url # str
		self.is_explicit = is_explicit # bool
		self.track_duration = track_duration # int

	def __str__(self):
		return "{} by {} | {} ms".format(self.track_title, self.artist_name, self.track_duration)

# Step 2
# ----------------------
# Create a sample instance of the Song class

# Using hte following information to save in the variable
# sample_inst:

# The artist name is "Queen"
# The song title is "Bohemian Rhapsody"
# The track url is https://itunes.apple.com/us/album/bohemian-rhapsody/932648190?i=932648449&uo=4
# The track time is 40000
# The track is not explicit

artist = "Queen"
url = "https://itunes.apple.com/us/album/bohemian-rhapsody/932648190?i=932648449&uo=4"
title = "Bohemian Rhapsody"
explicit = False
time = 40000

sample_inst = Song(artist, title, url, explicit, time)

# print class
print('\n'*2+'='*30)
print('Printing class')
print('-'*30)
print(sample_inst)

# print attributes
print('\n'*2+'='*30)
print('Printing attributes')
print('-'*30)

print(sample_inst.artist_name)
print(sample_inst.track_title)
print(sample_inst.track_duration)



# Step 3
# ---------------------------
# Fetch Song Data from iTunes and return Song instances

# 3.1 Modify get_from_itunes() from our previous discussion so that
# the function returns a list of Song objects instead of just the song titles

# HINT: Song objects should map to the following keys from the  iTunes API

def get_from_itunes(name, mtype="song"):
	baseurl = "https://itunes.apple.com/search"
	parameters = {}
	parameters['term'] = name
	parameters['entity'] = mtype
	print("Making a request to iTunes API...")
	response = requests.get(baseurl, params=parameters)
	python_obj = json.loads(response.text)

	# use python_obj to create instances of the Song class

	# 1. Investigate json object to find out song data
	#return json.dumps(python_obj, indent=2)
	#return python_obj['results'][0].keys()

	print('\n'*2+'='*30)
	print('Printing json_obj')
	print('-'*30)
	print(python_obj)
	fn = 'json_object.json'
	fh = open(fn, 'w')
	fh.write(json.dumps(python_obj))


get_from_itunes('Queen')