# Exercise 1 - Add lengths of strings in a list 

lst = ["hello", "hi", "to", "you"]

accum = 0

for s in lst:
	accum += len(s)

print(accum)


# Excercise 2 - Translate code to English

p = "Hello to everyone in SI 506. Enjoy the snow."
for orange in p:
	print(orange)

n = 0
pst = "Goodbye to everyone in SI 506. Enjoy the snow."
for itemch in pst:
	n = n + 1
print(n)

# English Description:
# I have a variable p, which gets assigned to a string: 
# "Hellow everyone in SI 506. Enjoy the snow."
# Then, for every character in my string p, I will print that character.
# Next, I have a variable n, which gets assigned to an integer of value 0.
# I also have a variable pst, which gets assgined to the string:
# "Goodbye to everyone in SI 506. Enjoy the snow."
# Now, for every character I see in the string pst, 
# I will re-assign the value the current value associated to the integer n
# plus 1.
# This means that when I see the character 'G', n is no longer assigned to 0, but 1
# Then, when I see the character 'o', n is no longer assigned to 1, but 2
# And so on and so forth, until I get to the last character of pst,
# which happens to be a period.
# At that point, n will be assigned to the value 46, which is the total number
# of characters in the string pst.