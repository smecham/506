import codecs, sys
import json
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# This week we're going to be creating restaurant objects from restaurants located in the Ann Arbor area! 
# We've provided you with a file called 'zomato_data.json.' Your job is to create a restaurant object 
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
		self.res_id = restaurant_diction['restaurant']['R']['res_id']
		self.name = restaurant_diction['restaurant']['name']
		self.address = restaurant_diction['restaurant']['location']['address']
		self.city = restaurant_diction['restaurant']['location']['city']
		self.aggregate_rating = restaurant_diction['restaurant']['user_rating']['aggregate_rating']
		self.num_votes = restaurant_diction['restaurant']['user_rating']['votes']
	# Complete with code...

	def __str__(self):
		return "{} is located in {}, {}. It has an average rating of {}".format(self.name, self.address, self.city, self.aggregate_rating)


####### TEST OUT THE INSTANCE ######

# Write some code to test out whether or not that instance works as you expect. 
# What code should you write?

fn = 'zomato_data.json'
fh = open(fn, 'r', encoding="utf-8")
fc = fh.read()
fh.close()
fc = json.loads(fc)

restaurant = Restaurant(fc['restaurants'][0])
print(restaurant)



####### (if time) DEFINE A FUNCTION #######
# Create a function (NOT a method, NOT inside a class) called print_popular_restaurant_info() that prints the top restuarants 
# based on a restaurant's rating from the Zamato API. 
# This function takes two parameters: a list of all restaurant instances you got from the data in zomato_annarbor.json, 
# and an integer  that will determine how many restaurants are printed.
# It should sort the restaurants by the aggregate rating and break any ties by the number of votes. 
# HINT: Check out sorting, and Sorting Instances, in the textbook!
# The function should return None -- it's for printing (for people!).
# But it should PRINT the input number of top restaurants, as shown in sample_output.txt.

# use list comprehension to create list of restaurant instances
#lst_restaurants = [Restaurant(elem) for elem in fc['restaurants']]
#for obj in lst_restaurants:
#	print(obj)

def print_popular_restaurant_info(rest_insts, num=10):
	#pass # replace with code

	# HINT: when you want to break ties, you need to sort your data twice. 
		# The first sort, secondary in terms of elements ordering, follows the tie breaking criterion
		# The second sort, primary in terms of elemtns ordering, is the primary order in which you need your data

	# secondary sort: break ties by the number of votes
	sorted_lst = sorted(rest_insts, key=lambda obj: obj.num_votes, reverse=True)
	# primary sort: restaurants by the aggregate rating
	sorted_lst2 = sorted(sorted_lst, key=lambda obj: obj.aggregate_rating, reverse=True)
	i = 1
	for elem in sorted_lst2[:num]:
		print("{}) {} is located on {}, {}. It has an average aggregate rating of {}, given by {} votes".format(i, elem.name, elem.address, elem.city, elem.aggregate_rating, elem.num_votes))
		#print(i, ")", elem.name, "is located on", elem.address, elem.city, ". It has an average aggregate rating of", elem.aggregate_rating, "given by", elem.num_votes)
		i += 1

#print_popular_restaurant_info(lst_restaurants)

####### MORE STARTER CODE: OPEN INPUT FILE, PRINT RESULTS #######

lst_restaurant_objects = [Restaurant(elem) for elem in fc['restaurants']] #list of restaurant instances 

## Write code to append to lst_restaurant_objects a list of restaurant instances
## HINT: You'll need to iterate over some part of the zamato data from the file supplied,
## and you'll need to invoke the class definition constructor from above

# Uncomment this line to invoke your function defined above
print_popular_restaurant_info(lst_restaurant_objects) #uncommenting this line should give you the expected output seen in 'sample_output.txt'
