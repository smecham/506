# import statements
import json
import requests

## [PROBLEM 1]
print("\n***** PROBLEM 1 *****\n")

f= open("sample_diction.json", "r")
read_file= f.read()
sample_photo_rep = json.loads(read_file)
f.close()
print(sample_photo_rep)

## [PROBLEM 2]
print("\n***** PROBLEM 2 *****\n")

FLICKR_KEY = "574271968c0be721187922f04180888b"

if FLICKR_KEY == "" or not FLICKR_KEY:
    FLICKR_KEY = input("Enter your flickr API key now, or paste it in the assignment .py file to avoid this prompt in the future. (Do NOT include quotes around it when you type it in to the command prompt!) \n>>")

## [PROBLEM 3] - Photo data investigation
print("\n***** PROBLEM 3 *****\n")

all_tags = sample_photo_rep['photo']['tags']['tag']
sample_tags_list = []
for each_tag in all_tags:
    sample_tags_list.append(each_tag['_content'])
print(sample_tags_list)

## [PROBLEM 4] - More Flickr data investigation
print("\n***** PROBLEM 4 *****\n")

river_pics= open("sample_flickr_response.json", "r")
read_it= river_pics.read()
search_result_diction = json.loads(read_it)
river_pics.close()
print(search_result_diction)

all_photos = search_result_diction['photos']['photo']
sample_photo_ids = []
for each_photo in all_photos:
    sample_photo_ids.append(each_photo['id'])
print(sample_photo_ids)

## [PROBLEM 5] - Set up the pattern for caching data
print("\n***** PROBLEM 5 *****\n")

CACHE_FNAME = "pset8_cached_data.json"

try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

## [PROBLEM 6]
print("\n***** PROBLEM 6 *****\n")

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get_flickr_data(tags_string, per_page=50):
    baseurl= "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = FLICKR_KEY
    params_diction["tags"] = tags_string
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"]= per_page
    params_diction["format"] = "json"
    unique_ident = params_unique_combination(baseurl,params_diction)
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        resp = requests.get(baseurl, params_diction)
        try_this = resp.text
        try_this_fixed= try_this[14:-1]
        CACHE_DICTION[unique_ident] = json.loads(try_this_fixed)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

sunny=get_flickr_data("sunshine")
stormy=get_flickr_data("stormy")
print(sunny)
print(stormy)

## [PROBLEM 7]
print("\n***** PROBLEM 7 *****\n")

flickr_mountains_result=get_flickr_data("mountains")
print(flickr_mountains_result)

## [PROBLEM 8]
print("\n***** PROBLEM 8 *****\n")

mountain_tags= flickr_mountains_result['photos']['photo']
photo_ids=[]
for each_photo in mountain_tags:
    photo_ids.append(each_photo['id'])
print(photo_ids)

## [PROBLEM 9]
print("\n***** PROBLEM 9 *****\n")

def get_photo_data_with_caching(photo_id):
    baseurl= "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = FLICKR_KEY
    params_diction["photo_id"] = photo_id
    params_diction["method"] = "flickr.photos.getInfo"
    params_diction["format"] = "json"
    unique_ident = params_unique_combination(baseurl,params_diction)
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        resp = requests.get(baseurl, params_diction)
        try_this = resp.text
        try_this_fixed= try_this[14:-1]
        CACHE_DICTION[unique_ident] = json.loads(try_this_fixed)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

hello=get_photo_data_with_caching('27020181468')
print(hello)
