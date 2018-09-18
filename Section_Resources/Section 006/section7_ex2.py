states = {
	"California" : 39536653,
	"Texas" : 28304596,
	"Florida" : 20984400, 
	"New York" : 19849399,
	"Pennsylvania" : 12805537,
	"Illinois" : 12802023,
	"Ohio" : 11658609,
	"Georgia" : 10429379,
	"North Carolina" : 10273419,
	"Michigan" : 9962311,
	"New Jersey" : 9005644,
	"Virginia" : 8470020,
	"Washington" : 7405743,
	"Arizona" : 7016270,
	"Massachusetts" : 6859819,
	"Tennessee" : 6715984 ,
	"Indiana" : 6666818,
	"Missouri" : 6113532,
	"Maryland" : 6052177,
	"Wisconsin" : 5795483,
	"Colorado" : 5607154,
	"Minnesota" : 5576606,
	"South Carolina" : 5024369,
	"Alabama" : 4874747,
	"Louisiana" : 4684333,
	"Kentucky" : 4454189,
	"Oregon" : 4142776,
	"Oklahoma" : 3930864,
	"Connecticut" : 3588184,
	"Puerto Rico" : 3337177,
	"Iowa" : 3145711,
	"Utah" : 3101833,
	"Arkansas" : 3004279,
	"Nevada" : 2998039,
	"Mississippi" : 2984100,
	"Kansas" : 2913123,
	"New Mexico" : 2088070,
	"Nebraska" : 1920076,
	"West Virginia" : 1815857,
	"Idaho" : 1716943,
	"Hawaii" : 1427538,
	"New Hampshire" : 1342795,
	"Maine" : 1335907,
	"Rhode Island" : 1059639,
	"Montana" : 1050493,
	"Delaware" : 961939,
	"South Dakota" : 869666,
	"North Dakota" : 755393,
	"Alaska" : 739795,
	"District of Columbia" : 693972,
	"Vermont" : 623657,
	"Wyoming" : 579315,
	"Guam" : 167358,
	"U.S. Virgin Islands" : 107268,
	"American Samoa" : 51504,
	"Northern Mariana Islands" : 52263,
	"Midway Atoll" : 40,
	"Johnston Atoll" : 0,
	"Wake Island" : 150,
	"Palmyra Atoll" : 20
}


# Fix order of elements into a list
states_and_populations = list(states.items())

# Sort list in descending order 
# according to each character's frequency
sorted_dictionary = sorted(states_and_populations, key = lambda tup: tup[1], reverse=True)


# ==============================================================
# To verify that sorted_dictionary is effectively sorted:

#print("="*30)

# Method 1:
#for state, population in sorted_dictionary:
#	print(str(state) + " has a population of " + str(population) + " people")

# Method 2:
#for tup in sorted_dictionary:
#	print(str(tup[0]) + " has a population of " + str(tup[1]) + " people")

#print("="*30)
# ==============================================================


# Get top 10
top10 = sorted_dictionary[:10]


# STEP 3: Visualize top 10
# -----------------------------

# Retrieve the frequency of the most frequent character
most_populated_tuple = top10[0]
most_populated_state = most_populated_tuple[1]

# Calculate relative frequency of each character:
# Relative frequency = (frequency of one character / frequency of most frequent character) * 20

for state, population in top10:
	relative_population_weight = (population/most_populated_state) * 20
	relative_population_weight = int(relative_population_weight)
	# Format output
	output = state + " : " + str("#"*relative_population_weight)
	print(output)


	