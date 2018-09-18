# __author__ = "Jackie Cohen"

## SI 506 W18
## Problem Set 10

import requests
import requests_oauthlib
import webbrowser
import json
import twitter_info
import csv

# [PROBLEM 1]
print("\n\n**** PROBLEM 1 ****\n")

CACHE_FNAME = "ps10_program_cache.json"
try:
    f = open(CACHE_FNAME, 'r')
    fstr = f.read()
    f.close()
    CACHE_DICTION = json.loads(fstr)
except:
    CACHE_DICTION = {}

client_key = twitter_info.consumer_key
client_secret = twitter_info.consumer_secret

if not client_secret or not client_key:
    print ("You need to fill in client_key and client_secret. See instructions in twitter_info.py")
    exit()

def get_tokens():
    oauth = requests_oauthlib.OAuth1Session(client_key, client_secret=client_secret)
    request_token_url = 'https://api.twitter.com/oauth/request_token'
    fetch_response = oauth.fetch_request_token(request_token_url)
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')
    base_authorization_url = 'https://api.twitter.com/oauth/authorize'
    authorization_url = oauth.authorization_url(base_authorization_url)
    webbrowser.open(authorization_url)
    verifier = input('Please input the verifier>>> ')
    oauth = requests_oauthlib.OAuth1Session(client_key,
                              client_secret=client_secret,
                              resource_owner_key=resource_owner_key,
                              resource_owner_secret=resource_owner_secret,
                              verifier=verifier)

    access_token_url = 'https://api.twitter.com/oauth/access_token'
    oauth_tokens = oauth.fetch_access_token(access_token_url)
    resource_owner_key = oauth_tokens.get('oauth_token')
    resource_owner_secret = oauth_tokens.get('oauth_token_secret')
    return (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier)

if "credentials" in CACHE_DICTION:
        client_key, client_secret, resource_owner_key, resource_owner_secret, verifier = CACHE_DICTION["credentials"]
else:
    tokens = get_tokens()
    client_key, client_secret, resource_owner_key, resource_owner_secret, verifier = tokens
    CACHE_DICTION["credentials"] = tokens
    dumped_cache = json.dumps(CACHE_DICTION)
    f = open(CACHE_FNAME,'w')
    f.write(dumped_cache)
    f.close()

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get_cache_twitter_search(search_term,num=25):
    base_url = "https://api.twitter.com/1.1/search/tweets.json"
    params_diction = {}
    params_diction['q'] = search_term
    params_diction['count'] = num

    unique_ident = params_unique_combination(base_url,params_diction)
    if unique_ident in CACHE_DICTION:
        return CACHE_DICTION[unique_ident]
    else:
        oauth = requests_oauthlib.OAuth1Session(client_key,
                            client_secret=client_secret,
                            resource_owner_key=resource_owner_key,
                            resource_owner_secret=resource_owner_secret)
        resp = oauth.get(base_url, params = params_diction)
        twitter_data = resp.text
        twitter_diction = json.loads(resp.text)
        CACHE_DICTION[unique_ident] = twitter_diction
        cache_dump = json.dumps(CACHE_DICTION)
        f = open(CACHE_FNAME,'w')
        f.write(cache_dump)
        f.close()
        return CACHE_DICTION[unique_ident]

# [PROBLEM 2]
print("\n\n**** PROBLEM 2 ****\n")

twitter_music_data= get_cache_twitter_search("music", num=50)
#print(twitter_music_data)

# [PROBLEM 3]
print("\n\n**** PROBLEM 3 ****\n")

class Tweet(object):
    def __init__(self, tweet_diction):
        self.text =  tweet_diction["text"]
        self.username= tweet_diction["user"]["screen_name"]
        self.favs= tweet_diction["favorite_count"] #IS THIS THE RIGHT FAVORITE_COUNT TO USE? THERE ARE DUPLICATE KEYS NESTED DIFFERENTLY IN twitter_music_data
        hashtag_list=[]
        for hashtags in tweet_diction["entities"]["hashtags"]:
            hash_text=hashtags["text"]
            hashtag_list.append(hash_text)
        self.hashtags= hashtag_list

    def most_common_letter(self):
        tweet_text=self.text
        frequencies={}
        for each_char in tweet_text:
            if each_char in frequencies:
                frequencies[each_char] = frequencies[each_char] + 1
            else:
                frequencies[each_char] = 1
        counter=list(frequencies.keys())
        best_so_far=counter[0]
        for each_key in counter:
            if frequencies[each_key] > frequencies[best_so_far]:
                best_so_far=each_key
            return best_so_far

    def __str__(self):
        return (self.text + " - posted by - " + self.username + " - " + self.most_common_letter() + " is the most common letter in it.")

st = open("sample_tweet.json")
one_tweet = json.loads(st.read())
st.close()
tw = Tweet(one_tweet)
print(tw)
print(tw.favs)
print(tw.hashtags)
print(tw.text)
print(tw.username)
print(tw.most_common_letter())

# [PROBLEM 4]
print("\n\n**** PROBLEM 4 ****\n")

tweet_insts=[]
for tweet in twitter_music_data["statuses"]:
    tweet_instance= Tweet(tweet)
    tweet_insts.append(tweet_instance)

#LIST COMPREHENSION METHOD --> COULD NOT GET TO WORK
#tweet_insts= [Tweet(tweet_diction) for tweet_diction in twitter_music_data["statuses"]]

# [PROBLEM 5]
print("\n\n**** PROBLEM 5 ****\n")

for t in tweet_insts[:5]:
    print(t)
for t in tweet_insts[-5:]:
    print(t)

outfile= open('tweet_info.csv', 'w', newline='')
writer = csv.writer(outfile, delimiter=',')
writer.writerow(("Username", "Text", "Number of hashtags", "Number of favorites"))
for each_tweet in tweet_insts:
    writer.writerow((each_tweet.username, each_tweet.text.strip('\n'), len(each_tweet.hashtags), each_tweet.favs))
outfile.close()

#METHOD WITHOUT USING CSV MODULE --> COULD NOT GET THIS TO WORK
#outfile = open("tweet_info.csv","w")
#outfile.write('"Username", "Text", "Number of hashtags", "Number of favorites"\n')
#for each_tweet in tweet_insts:
    #outfile.write('"{}", "{}", "{}"\n'.format(each_tweet.username, each_tweet.text, len(each_tweet.hashtags), each_tweet.favs))
#outfile.close()

fileref = open("tweet_info.csv")
lines = fileref.readlines()
fileref.close()
print(len(lines))
