import json

f = open('tweets.txt')
tweets = []
for line in f:
	tweet = json.loads(line)
	tweets.append(tweet)

# Now tweets contains a list of tweet dictionaries



# Iterate over them to print the text of each tweet
# (Remember what you did in section8_sample.py?)


# Iterate over them to print the favorite count of each tweet


# OK, put those together: Iterate over the list of tweet dictionaries and print each one's favorite count and then its text


########################
#### Writing a CSV file
########################

# Open the file for writing


# Iterate over the list of tweet dictionaries just as before

#### Create a string that contains each tweet's favcount + comma + text
#### Write it to the file with a newline


# Close the file


########
# Extra
########

# How will you print the 5 most common hashtags in the tweets? (See handout.)
