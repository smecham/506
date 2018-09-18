# https://developer.oxforddictionaries.com/documentation/making-requests-to-the-api

# The Oxford API comes with sample python code

username = ""
baseurl = ""
appID = "" # required
appKeys = "" # required

# Required parameters
#----------------------
#app_id - unique identifier for your application
#app_key # key for your application

# There are multiple end points for this API
#-----------------------------------------------
# Lemmatron
	# Check a word exists in the dictionary and retrieve its root form
	# Apply optional filters to Lemmatron response

# Dictionary entries - for definitions ------- !!!!!
	# Retrieve dictionary information for a given word
		# Endpoint: entries (str, must be appended as a suffix to URL. Not sure if I need '/' before and after)
		# Params: source_lang, word_id, app_id, app_key (str all of them)
	# Specify GB or US dictionary for English entry search
	# Apply filters to response

# Thesaurus
	# Retrieve words that are similar
	# Retrieve words that mean the opposite
	# Retrieve synonyms and antonyms for a given word

# Search
	# Retrieve possible matches to input
	# Retrieve possible translation matches to input

# Translation
# Wordlist
# The Sentence Dictionary
# LexiStats
# Utility
# 

# Other parameters
#----------------------
# word_id - used whenever you request information about a specific word. Word id's must be URL encoded
# 
