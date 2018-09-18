# SI 506 - Programming I
# Section 6 - 2/13


# STEP 1: Creating a folder and a file
# ---------------------------------------

# I need to invoke the encoding parameter while opening the file. 
# Otherwise, I get an error like so:
# "UnicodeDecodeError: 'charmap' codec can't decode byte ..." 
file_object = open("alice.txt","r",encoding="utf8")

# This was the original call to the open function, 
# the file handle would be created, but the file would include characters
# in a different encoding, and thus the read method would not work:
#file_object = open("alice.txt","r")

# Assuming the encoding parameter is invoked in the 
# encoding method, the read method will work 
text = file_object.read()

# Sever the connection between python and the file
file_object.close()


# STEP 2: Find top 10
# -----------------------------

# Make all text lowercase
text = text.lower()

# Placeholder for characters and frequencies
dictionary = {}

# Calculate frequency of every character
for char in text:
	if char not in dictionary:
		dictionary[char] = 1
	else:
		dictionary[char] += 1

# Fix order of elements into a list
chars_and_frequencies = list(dictionary.items())

# Sort list in descending order 
# according to each character's frequency
sorted_dictionary = sorted(chars_and_frequencies, key = lambda x: x[1], reverse=True)


# ==============================================================
# To verify that sorted_dictionary is effectively sorted:

# Method 1:
#for char, frequency in sorted_dictionary:
#	print(str(char) + " appears " + str(frequency) + " times")

# Method 2:
#for tup in sorted_dictionary:
#	print(str(tup[0]) + " appears " + str(tup[1]) + " times")
# ==============================================================


# Get top 10
top10 = sorted_dictionary[:10]


# STEP 3: Visualize top 10
# -----------------------------

# Retrieve the frequency of the most frequent character
most_frequent_tuple = top10[0]
most_frequent_char = most_frequent_tuple[1]

# Calculate relative frequency of each character:
# Relative frequency = (frequency of one character / frequency of most frequent character) * 20

for char, frequency in top10:
	relative_frequency = (frequency/most_frequent_char) * 20
	relative_frequency = int(relative_frequency)
	# Format output
	output = char + " : " + str("#"*relative_frequency)
	print(output)


	