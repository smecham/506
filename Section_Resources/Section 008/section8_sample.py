import json

text = open('sample_tweet.txt').read()
tweet = json.loads(text)

# Now tweet is a dictionary object


