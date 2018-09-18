# __author__ = "Jackie Cohen"

## SI 506 W18
## Problem Set 10

# import statements
import requests
import requests_oauthlib
import webbrowser
import json
import twitter_info

# [PROBLEM 1]
print("\n\n**** PROBLEM 1 ****\n")
# Below, we have provided code that provides the possibility to get and cache data from Twitter, with a few function definitions:
# - params_unique_combination
# - get_tokens
# - get_cache_twitter_search

# You should look through the code and ensure you understand what each function does, and which function to invoke to get data from Twitter.
# Note that the code is somewhat commented to indicate what each piece does.

# Caching setup
CACHE_FNAME = "ps10_program_cache.json" # Do not change -- may need to delete the FILE if it ends up in a bad state
try:
    f = open(CACHE_FNAME, 'r')
    fstr = f.read()
    f.close()
    CACHE_DICTION = json.loads(fstr)
except:
    CACHE_DICTION = {}

## Setup of Twitter credentials from twitter_info file
client_key = twitter_info.consumer_key # what Twitter calls Consumer Key
client_secret = twitter_info.consumer_secret # What Twitter calls Consumer Secret

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

# Check if there are cached credentials or not and access them in appropriate variables. Set up global variables to hold these values for creating OAuth instances.
if "credentials" in CACHE_DICTION:
        client_key, client_secret, resource_owner_key, resource_owner_secret, verifier = CACHE_DICTION["credentials"]
else:
    tokens = get_tokens()
    client_key, client_secret, resource_owner_key, resource_owner_secret, verifier = tokens # Tuple unpacking assignment
    CACHE_DICTION["credentials"] = tokens
    dumped_cache = json.dumps(CACHE_DICTION)
    f = open(CACHE_FNAME,'w')
    f.write(dumped_cache)
    f.close()

# params_unique_combination function for unique identifiers based on raw materials
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
        # Remember we need to use an oauth object instance to make the request, using requests_oauthlib
        oauth = requests_oauthlib.OAuth1Session(client_key,
                            client_secret=client_secret,
                            resource_owner_key=resource_owner_key,
                            resource_owner_secret=resource_owner_secret) # Using the global vars from getting credentials / getting credentials from cache
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

# Invoke the correct function from above to get data about 50 tweets from Twitter, searching for "music"
# Save the result in a variable: twitter_music_data

## NOTE: It's fine to print out all or part of twitter_music_data to investigate here, but you should COMMENT OUT all print statements after you're done to make it easier to grade! We MAY deduct 25 points for multiple print statements of an entire set of data from a twitter search outside a problem.


# [PROBLEM 3]
print("\n\n**** PROBLEM 3 ****\n")

## We've included a file sample_tweet.json, similar to the file you saw in the last problem set.
## It represents the structure of ONE single tweet (while the data you just accessed and saved in the twitter_music_data variable contains _fifty_ different tweets, all with a almost identical *structure* to this one, of course).
## Here, I recommend taking some time to investigate the data in that sample tweet before continuing on to the rest of the program.


## After getting a better understanding of that data, your goal is to complete the definition of this class Tweet, following the instructions.

class Tweet(object):
    def __init__(self, tweet_diction):
        self.text =  tweet_diction["text"]
        # Complete this constructor to add the following instance variables in addition to self.text:
        # self.username, holding the string of the USERNAME of the person who posted the tweet
        # self.favs, holding the INTEGER representing the number of favorites this tweet has
        # self.hashtags, holding a LIST OF STRINGS representing each hashtag in the tweet. If there are no hashtags in the tweet, this should hold an empty list.
        ## HINT: Looking at the exercise about class Photo from Wednesday and the section exercise where you worked with Twitter data may both be helpful here.

    def most_common_letter(self):
        pass # Replace with code
        # This method should return the most common non-space character in the text of this tweet.

    def __str__(self):
        pass # replace with code
        # Fill in this string method so that when a Tweet instance is printed, it prints, without the [ ]s:
        # [text of tweet] - posted by - [username] - [common letter] is the most common letter in it.
        # HINT: You should have access to all of those []ed values already -- either in an instance variable, of course, or by invoking another class method.

## If you uncomment the following code, you can test out a few things in your class definition:
# st = open("sample_tweet.json")
# one_tweet = json.loads(st.read())
# st.close()
# tw = Tweet(one_tweet)
# print(tw.text)
# print(tw.username)
# print(tw.most_common_letter())
# print(tw)

## Feel free to add more code here to test out that instance if you want.

# [PROBLEM 4]
print("\n\n**** PROBLEM 4 ****\n")
# Now, go back to using the twitter_music_data value you got in Problem 2.
# You may want to do some data investigation here.
# HINT: Your section exercise dealing with Twitter data may be somewhat helpful here, as will jsoneditoronline.org, but it's always useful to do investigation again.
# Your section exercise creating instances of class Song may also be helpful.

# YOUR GOAL here is to iterate over the tweet dictionaries in twitter_music_data, and create a list of 50 Tweet instances from them.
# You should save the list of tweet instances in a variable: tweet_insts.


# [PROBLEM 5]
print("\n\n**** PROBLEM 5 ****\n")
## Problem 5 (a)
# You can test whether the above worked by uncommenting the following code:
# for t in tweet_insts[:5]:
#     print(t) # Should see a nice string  each time
# for t in tweet_insts[-5:]:
#     print(t)

## NOTE: If you print the ENTIRE LIST at once, without iterating over it, you will not see a list of strings! That's because the print() function must be invoked on a specific instance in order to trigger the __str__ function for it invoking.

## Problem 5 (b)

# Open a .CSV file called tweet_info.csv for writing. IT MUST BE CALLED EXACTLY THAT OR TESTS WILL NOT PASS!
# Use your list of instances, saved in tweet_insts, and your knowledge of file operations, to write a CSV file containing data about these 50 tweets, with the following columns and corresponding values:
# Username
# Text (WITHOUT NEWLINES -- all should be replaced!)
# Number of hashtags [NOTE: NUMBER, not hashtags themselves]
# Number of favorites


# NOTE: Remember that newlines are important to consider when writing to a CSV file, both when you remove them from text data and when you write things to a file that should be on separate lines.
# Remember to close the file when you are done writing to it!



## Finally, NOTE: Imagine what you could do with this info, especially if you had even more data... e.g. You could see what kind of correlation there is between number of hashtags and number of favorites, perhaps!
## If you want to check this out, you can upload the .CSV file to Google Drive or open it in Excel/Numbers and use the charting functionality to see what it looks like!
