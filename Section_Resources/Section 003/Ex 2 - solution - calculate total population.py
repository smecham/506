# Dictionary provided here with names and populations
states = { "California" : 39536653, "Texas" : 28304596, "Florida" : 20984400, "New York" : 19849399, "Pennsylvania" : 12805537, "Illinois" : 12802023, "Ohio" : 11658609, "Georgia" : 10429379, "North Carolina" : 10273419, "Michigan" : 9962311, "New Jersey" : 9005644, "Virginia" : 8470020, "Washington" : 7405743, "Arizona" : 7016270, "Massachusetts" : 6859819, "Tennessee" : 6715984 , "Indiana" : 6666818, "Missouri" : 6113532, "Maryland" : 6052177, "Wisconsin" : 5795483, "Colorado" : 5607154, "Minnesota" : 5576606, "South Carolina" : 5024369, "Alabama" : 4874747, "Louisiana" : 4684333, "Kentucky" : 4454189, "Oregon" : 4142776, "Oklahoma" : 3930864, "Connecticut" : 3588184, "Puerto Rico" : 3337177, "Iowa" : 3145711, "Utah" : 3101833, "Arkansas" : 3004279, "Nevada" : 2998039, "Mississippi" : 2984100, "Kansas" : 2913123, "New Mexico" : 2088070, "Nebraska" : 1920076, "West Virginia" : 1815857, "Idaho" : 1716943, "Hawaii" : 1427538, "New Hampshire" : 1342795, "Maine" : 1335907, "Rhode Island" : 1059639, "Montana" : 1050493, "Delaware" : 961939, "South Dakota" : 869666, "North Dakota" : 755393, "Alaska" : 739795, "District of Columbia" : 693972, "Vermont" : 623657, "Wyoming" : 579315, "Guam" : 167358, "U.S. Virgin Islands" : 107268, "American Samoa" : 51504, "Northern Mariana Islands" : 52263, "Midway Atoll" : 40, "Johnston Atoll" : 0, "Wake Island" : 150, "Palmyra Atoll" : 20}

# Write the remainder of your code here...
state_inp = input("Please enter a list, comma separated, of the areas whose population you want: ")

# Get a list of relevant names only
states_list = state_inp.split(", ") # This is tricky and could also be done with split on comma and remove space
total_population_we_care_about = 0 # Should accumulate only pops under 5mil

for name in states_list:
    if states[name] < 5000000: # if the population looked up is less than 5 mil
        total_population_we_care_about = total_population_we_care_about + states[name]

# Plus you imagine a variety of error checking
# A "try again" message or something like that
print(total_population_we_care_about )