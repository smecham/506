import json

# This week we're going to be creating restaurant objects from restaurants located in the Ann Arbor area! 
# We've provided you with a file called 'zomato_annarbor.json.' Your job is to create a restaurant object 
# for each of the restaurants in the json data, and print the top 10 restaurants based on their rating. 


####### CREATE A CLASS #######
# Your restaurant class should contain the following instance variables and methods:

# Methods:
#   __init__()
#   __str__() 

# Variables:
#   res_id 
#   name 
#   address
#   city
#   aggregate_rating
#   num_votes (votes)

class Restaurant(object):
	def __init__(self, restaurant_diction):
		pass 
	# Complete with code...


####### TEST OUT THE INSTANCE ######

# Write some code to test out whether or not that instance works as you expect. 
# What code should you write?



####### (if time) DEFINE A FUNCTION #######
# Create a function (NOT a method, NOT inside a class) called print_popular_restaurant_info() that prints the top restuarants 
# based on a restaurant's rating from the Zamato API. 
# This function takes two parameters: a list of all restaurant instances you got from the data in zomato_annarbor.json, 
# and an integer  that will determine how many restaurants are printed.
# It should sort the restaurants by the aggregate rating and break any ties by the number of votes. 
# HINT: Check out sorting, and Sorting Instances, in the textbook!
# The function should return None -- it's for printing (for people!).
# But it should PRINT the input number of top restaurants, as shown in sample_output.txt.

def print_popular_restaurant_info(rest_insts, num):
	pass # replace with code



####### MORE STARTER CODE: OPEN INPUT FILE, PRINT RESULTS #######

lst_restaurant_objects = [] #list of restaurant instances 

## Write code to append to lst_restaurant_objects a list of restaurant instances
## HINT: You'll need to iterate over some part of the zamato data from the file supplied,
## and you'll need to invoke the class definition constructor from above

# Uncomment this line to invoke your function defined above
# print_popular_restaurant_info(lst_restaurant_objects) #uncommenting this line should give you the expected output seen in 'sample_output.txt'