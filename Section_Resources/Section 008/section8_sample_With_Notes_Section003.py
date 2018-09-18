import json

text = open('sample_tweet.txt').read()
tweet = json.loads(text)

# Now tweet is a dictionary object

print("tweet keys",tweet.keys())

print("Tweet text is:")
print(tweet["text"])

print("what's the value of the entities key?")
print(tweet["entities"])
print(type(tweet["entities"]))
# THis is a dictionary -- tweet["entities"]
print(tweet["entities"].keys())

# I want to look in that dictionary
# I want to know about the value of the key "hashtags"
print("The value of the hashtags key in entities")
print(tweet["entities"]["hashtags"])
print(type(tweet["entities"]["hashtags"]))

# OK also:
# entities_thing = tweet["entities"]
# print(entities_thing["hashtag"])


# What's my problem again?
# For each hashtag in this one tweet,
# Print out its text.

## I want to translate this into code:
# for each_thing in # all of one tweet's hashtags??? :
#     # print its text

# The value of the key 'hashtags', which is inside the tweet's key 'entities'
# is a list of dictionaries.

# for each_thing in # all of one tweet's hashtags??? :
all_hashtags = tweet["entities"]["hashtags"]
for each_thing in all_hashtags:
#     # print its text
    print(each_thing,"each hashtag") # OK, what do I want to do to it each time?
    # I want to print the value assoc with the key 'text'

# To complete the problem,
for each_thing in all_hashtags: # could replace all_hashtags with tweet["entities"]["hashtags"]
    print(each_thing["text"])
