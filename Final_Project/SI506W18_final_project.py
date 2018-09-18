#Final Project | SI 506 | Stephanie Mecham

#import statements
import requests
import requests_oauthlib
import webbrowser
import json
import twitter_info
import csv

#set up cache dictionary, authorization function, and caching pattern

CACHE_FNAME = "SI506W18final_project_cache.json"
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

#Twitter API Request Function:

def get_from_twitter(search_term,num=25):
    base_url = "https://api.twitter.com/1.1/search/tweets.json"
    params_diction = {}
    params_diction['q'] = search_term
    params_diction['count'] = num

    unique_ident = params_unique_combination(base_url,params_diction)
    if unique_ident in CACHE_DICTION:
        print("Retrieving cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making request to Twitter API...")
        try:
            oauth = requests_oauthlib.OAuth1Session(client_key, client_secret=client_secret,resource_owner_key=resource_owner_key,resource_owner_secret=resource_owner_secret)
            resp = oauth.get(base_url, params=params_diction)
            twitter_data = resp.text
            twitter_diction = resp.json()
            CACHE_DICTION[unique_ident] = twitter_diction
            cache_dump = json.dumps(CACHE_DICTION)
            f = open(CACHE_FNAME,'w')
            f.write(cache_dump)
            f.close()
            return CACHE_DICTION[unique_ident]
        except json.JSONDecodeError:
            print('Could not decode a row')

print(type(get_from_twitter('Trump'))) #testing function
print(get_from_twitter('Trump')) #testing function

twitter_data= get_from_twitter(input("Enter search keyword now:"), num=100)

#iTunes API Request Function:

def get_from_itunes(name, mtype='song', m=60):
    base_url = 'https://itunes.apple.com/search'
    params_diction = {}
    params_diction['term'] = name
    params_diction['entity'] = mtype
    params_diction['limit'] = m

    unique_ident = params_unique_combination(base_url,params_diction)
    if unique_ident in CACHE_DICTION:
        print("Retrieving cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making request to iTunes API...")
        try:
            resp = requests.get(base_url,params=params_diction)
            itunes_data = resp.text
            itunes_diction = resp.json()
            CACHE_DICTION[unique_ident] = itunes_diction
            cache_dump = json.dumps(CACHE_DICTION)
            f = open(CACHE_FNAME,'w')
            f.write(cache_dump)
            f.close()
            return CACHE_DICTION[unique_ident]
        except json.JSONDecodeError:
            print('Could not decode a row')

print(type(get_from_itunes('Jackson'))) #testing function
print(get_from_itunes('Jackson')) #testing function

#Tweet class:

class Tweet(object):
    def __init__(self, tweet_diction):
        self.text =  tweet_diction["text"]
        self.username = tweet_diction["user"]["screen_name"]
        hashtag_list=[]
        for hashtags in tweet_diction["entities"]["hashtags"]:
            hash_text=hashtags["text"]
            hashtag_list.append(hash_text)
        self.hashtags= hashtag_list
        self.username= tweet_diction["user"]["screen_name"]
        self.favs= tweet_diction["favorite_count"]


    def number_of_hashtags(self):
        return len(self.hashtags)

    def longest_word(self):
        list_of_words = self.text.split()
        word_lengths={}
        for each_word in list_of_words:
            if "https" in each_word: #Don't want to include URL links in possible longest words!
                print("Do nothing")
            if "@" in each_word: #Don't want to include Twitter usernames in possible longest words!
                print("Do nothing")
            else:
                word_lengths[each_word] = len(each_word)
        counter=list(word_lengths.keys())
        best_so_far=counter[0]
        for each_key in counter:
            if word_lengths[each_key] > word_lengths[best_so_far]:
                best_so_far=each_key
        return best_so_far

    def most_common_letter(self): #THIS METHOD IS EXTRA
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
        return ("This tweet says ''" + self.text + "', is posted by " + self.username + ", and has " + str(self.number_of_hashtags()) + " hashtags. It's longest word is " + self.longest_word() + " and it's most common letter is " + self.most_common_letter() + ".")

#Song class:

class Song(object):
    def __init__(self, song_diction):
        self.song_name = song_diction["results"][0]["trackName"]
        self.artist_name= song_diction["results"][0]["artistName"]
        self.song_milli= song_diction["results"][0]["trackTimeMillis"]
        self.genre = song_diction["results"][0]["primaryGenreName"]

    def song_length(self):
        seconds = (self.song_milli / 1000)
        return seconds

    def __str__(self):
        return (self.song_name + " - performed by - " + self.artist_name + " is " + str(self.song_length()) + " seconds long and is considered to be " + self.genre + " genre.")

#List of Tweet Instances:

tweet_insts=[]
for tweet in twitter_data["statuses"]:
    if "RT" not in tweet["text"]:
        tweet_instance= Tweet(tweet)
        tweet_insts.append(tweet_instance)

for t in tweet_insts:
    print(t)

#Sort by Number of Hashtags:

sorted_by_hashtag = sorted(tweet_insts, key=lambda x: x.number_of_hashtags(), reverse=True)

for t in sorted_by_hashtag:
    print(t)

#List of Song Instances:

song_insts=[]
for each_tweet in sorted_by_hashtag:
    itunes_music_data=get_from_itunes(each_tweet.longest_word())
    if itunes_music_data is not None and len(itunes_music_data["results"]) > 0:
        song_instance = Song(itunes_music_data)
        song_insts.append(song_instance)
    else:
        print("There is no iTunes song for that word!")

for t in song_insts:
    print(t)

#Combining Lists into Tweets & Their Corresponding Songs:

data = [list(instance) for instance in zip(sorted_by_hashtag, song_insts)]

#Writing to a CSV file:

outfile= open('tweets_songs.csv', 'w', newline='')
writer = csv.writer(outfile, delimiter=',')
writer.writerow(("SI 506 Final Project - Playlist Based on Tweets", "Stephanie Mecham"))
writer.writerow(("Tweet Text", "Number of Hashtags", "Longest Word", "Song Name", "Song Artist", "Length of Song (seconds)", "Genre"))
for each_set in data:
    x = each_set[0]
    y = each_set[1]
    writer.writerow((x.text, x.number_of_hashtags(), x.longest_word(), y.song_name, y.artist_name, y.song_length(), y.genre))
outfile.close()
