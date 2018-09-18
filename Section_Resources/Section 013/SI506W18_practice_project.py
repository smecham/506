# For Part 2, you should create a file called `SI506W18_practice_project.py`. In that file, you should write code (including all/any imports you need) to get and cache all of the data you will need to get and cache for your project.

# It is OK to use code from class for this, but make sure you understand what it does.

# Your code should contain at least a couple comments explaining what it does.

# In this file, you should do some investigation on that data — get a good understanding of what data you can get and what pieces of it might be interesting to you, how to access them from the nested data, etc.

# This will be graded on 

#- Whether it runs and works
#- Whether it does indeed get and cache all data you have explained that you need for your project (in Part 1)
#- Whether there are print statements showing evidence that you understand the nested data you are working with

#It is OK to include comments with questions/curiosities, but you should prioritize understanding what your code does and how it will be used in your project. This is code you should be able to translate directly to your project file.

import codecs, sys
import requests
import json
import webbrowser
import oxford_api_credentials

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


# General variables
OUTPUT_FNAME = "SI506W18_finalproject_output.py" # for long term memory
CACHE_FNAME = "SI506W18finalproject_cache.json" # for long term memory
CACHE_DICTION = {} # for working memory

# Caching setup
try:
    f = open(CACHE_FNAME, 'r')
    fstr = f.read()
    f.close()
    CACHE_DICTION = json.loads(fstr)
except:
    CACHE_DICTION = {}


# Utility function definition provided for your use here (DO NOT CHANGE)
## Function to create a unique representation of each request without private data like API keys
def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

# Getting info from OED
def get_from_oxford(term):
	
	credentials = {}
	credentials["app_id"] = oxford_api_credentials.appID
	credentials["app_key"] = oxford_api_credentials.appKeys

	dp = {}
	dp['source_lang'] = "en"
	dp['word_id'] = term.lower().replace(" ","")

	url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'

	# This code formats the base URL to include the parameters. For some reason,
	# calling the the params parameter in the get method doesn't work for this function
	for k, v in dp.items():
		url = url + v + '/'
	url = url[:-1] # The code breaks if it ends iwth a slash, but each individual parameter should
				   # be separated by one
	
	search_id = params_unique_combination(url, dp)
	if search_id in CACHE_DICTION:
		query = CACHE_DICTION[search_id]
	else:
		query = requests.get(url, headers=credentials)
		print(query.status_code)
		query = json.loads(query.text)
		CACHE_DICTION[search_id] = query
		jsonstr = json.dumps(CACHE_DICTION)
		fhandle = open(CACHE_FNAME, 'w')
		#fhandle.write(jsonstr.encode('utf-8', 'ignore'))
		fhandle.write(jsonstr)
		fhandle.close()
	return query

oxford = get_from_oxford(input("Enter your search term: "))

print("Examples of data within the cached data")
print("="*30)

print("OED")
print("-"*30)
print("Term:", oxford['results'][0]["id"].capitalize())
print("Lexical category:", oxford['results'][0]['lexicalEntries'][0]['lexicalCategory'])
print("Definitions for this lexical category:")
count = 1
for i in range(len(oxford['results'][0]['lexicalEntries'][0]['entries'])):
	item = oxford['results'][0]['lexicalEntries'][0]['entries'][i]
	for definition in item['senses']:
		if "domains" in list(definition.keys()):
			print("Domain:", definition['domains'][0])
			count = 1
		print(count, "-", definition["definitions"][0].capitalize())
		count += 1
