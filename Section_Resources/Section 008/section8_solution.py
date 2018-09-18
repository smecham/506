# This is the solution to the steps involving multiple tweets (the file tweets.txt, steps 3+ on the handout)

import json

f = open('tweets.txt')
tweets = []
for line in f:
	tweet = json.loads(line)
	tweets.append(tweet)

# Now tweets contains a list of tweet objects 

# Part 1: most liked tweets
# Break ties alphabetically:
tweets = sorted(tweets, key=lambda t: t['text']) 
sorted_by_fav = sorted(tweets, key=lambda t: t['favorite_count'], reverse=True)
print('FavCount Tweet')
for t in sorted_by_fav[:5]:
	print(t['favorite_count'], '\t', t['text'])
print() # Just prints an extra blank line for clarity of output

# Part 2: writing a CSV
f = open("tweet_favcounts.csv",'w')
header_str = "FavCount,Tweet\n"
f.write(header_str)
# Code just like above, but building strings and writing to file...
for t in sorted_by_fav[:5]:
	f.write("{},{}\n".format(t["favorite_count"],t['text'])) # Use string formatting to put those values into the string you are writing to the file each time
f.close() # And close the file


# Part 3: most popular hashtags
hashtag_count = {}
for t in tweets:
	hashtags = t['entities']['hashtags']
	for hashtag in hashtags:
		ht_text = hashtag['text']
		if ht_text not in hashtag_count:
			hashtag_count[ht_text] = 0
		hashtag_count[ht_text] += 1

most_popular_hashtags = sorted(hashtag_count.items(), key=lambda item: item[1], reverse=True)
print('Hashtag\tCount')
for h in most_popular_hashtags[:5]:
	print(h[0], '\t', h[1])
