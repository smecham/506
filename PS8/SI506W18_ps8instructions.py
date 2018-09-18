# import statements
import json
import requests

## IMPORTANT NOTES:

## In general, this course expects you to run Python files via the command prompt. In some cases, even if you do not do so, assignments will work. This assignment, depending upon your setup, is VERY UNLIKELY to work if you do not run it via the command prompt (Git Bash or Terminal).

## Remember: run your program early and often to determine what it is doing and whether it is working as you expect it to! DO NOT turn your program in without first running it to make sure that all of the test output is shown and it runs properly. We do not grade files that do not run.

## We recommend reading through the whole file first, and reading directions carefully, and then beginning with the first problem, with an understanding of what you will be doing throughout the problem set.

## You should NOT be writing any additional calls to input (besides the one that already exists / will run if you do not include your flickr_key).

## Again, to run the tests, you can run the included Python file SI506W18ps8tests.py

#########

## [PROBLEM 1]
print("\n***** PROBLEM 1 *****\n") # (Print statements like this throughout the problem set are provided to help you figure out where things are when you see output. You should leave them alone.)

## We have provided a sample dictionary in the format that Flickr returns it, saved in a JSON file (much like the nested_data.json file you were provided in Problem Set 6).

## Write code to open the file sample_diction.json and load its contents as a Python object into the variable sample_photo_rep. Then close the file (that'll keep you from running into easily-avoidable errors later on!). There are unit tests for this problem.

## (You may also find it useful, for later in the problem set, to open the file "sample_diction.json" in a text editor, or copy and paste its contents into http://www.jsoneditoronline.org/ to see what the nested data in this dictionary will be structured like.)



## [PROBLEM 2] -- Code setup (get and paste in your Flickr API key)
print("\n***** PROBLEM 2 *****\n")
## Set up code so you, too, can access the Flickr API. (You have probably already done this in class, but it is necessary to complete this assignment.)

## You will need a Yahoo!/Hotmail account in order to sign in to Flickr. You need such an account in order to complete this assignment. But it does not need to be a "real" account that you will use for anything else besides this, and you do not need to use your real name for it if you do not want to.
## Follow the instructions in the Flickr chapter to get a key for the Flickr API so that you can get data from Flickr.
## There are no tests for this problem; your problem set will not work if you do not complete it.

# THIS IS VERY IMPOTANT FOR US TO BE ABLE TO AUTOGRADE YOUR FILE! Make sure you fill this in!
# We will not use your key for any nefarious purposes. You can regenerate it after you get a grade for this assignment.

FLICKR_KEY = ""
# Paste your flickr API key here, between those quotation marks, such that the variable flickr_key will contain a string (your flickr key!).

## DO NOT CHANGE ANYTHING ELSE ABOUT THE CODE IN THIS PROBLEM, BELOW THIS COMMENT.
## Normally you should not share API keys with others. But if you include your key in your problem set submission file here, we will not use it for anything nefarious, and we will show you how you can regenerate it later.
if FLICKR_KEY == "" or not FLICKR_KEY:
    FLICKR_KEY = input("Enter your flickr API key now, or paste it in the assignment .py file to avoid this prompt in the future. (Do NOT include quotes around it when you type it in to the command prompt!) \n>>")


## [PROBLEM 3] - Photo data investigation
print("\n***** PROBLEM 3 *****\n")

## The sample_photo_rep variable you defined in Problem 1 should contain a complex Python object. That represents data about a single photo on Flickr.

## Write code to access the nested data inside sample_photo_rep to create a list of all of the tags of that photo. Save the list of tags in a variable called sample_tags_list.

## You will need to do a bunch of nested data investigation and nested iteration in order to complete this. Copying the contents of the sample_diction.json file into jsoneditoronline.org may help. Remember, go slowly and step-by-step; understand, then extract, then understand the next bit...

## When you have completed this problem, the tags list in sample_tags_list should basically look like this: ['nature', 'mist', 'mountain']
## HINT: Check out the '_content' keys' values deep inside the nested dictionary... (Don't use the values of the "raw" keys.)
## There are tests for this problem.




## [PROBLEM 4] - More Flickr data investigation
print("\n***** PROBLEM 4 *****\n")

## We have also provided a file called sample_flickr_response.json. This file contains data that has been retrieved from the Flickr API in response to a request for 50 photos tagged with the word "river", but the data from the API has been altered slightly so that it is properly formatted in a JSON way (as discussed in class).

## NOTE that this is DIFFERENT data than the data from Problem 3 -- this is data that represents a search for photos, NOT detailed information abou the photos. The data in problem 3 represented a request for info about ONE photo only, and has more specific detail about that one photo.

## Write code to open that sample_flickr_response.json file and load the data inside that file into a variable called search_result_diction. Remember to close any file you open once you're done with it!



## After you have done that, the variable search_result_diction should now contain a very complex dictionary representing information about a bunch of photos that are tagged "river". Each photo has an id.

## Write code to create a list of all of the photo ids from each photo that the search_result_diction data represents, and save that list in a variable called sample_photo_ids.

## There are tests for this problem.




## [PROBLEM 5] - Set up the pattern for caching data
print("\n***** PROBLEM 5 *****\n")

## This problem set will now combine some of the work you've done already with work a lot like what you did in Problem Set 7 -- but this time you will be caching your data, so your code will only make a request to the internet when you don't already have the data you need.

## Translate the following English into code, as described in Caching Responses section of the textbook and in class, in order to set up a pattern so you can cache the data you get in this problem set.

## We suggest keeping the comments and writing the code translations above OR below OR to the left of each of them...

## This code will work in conjunction with code you write later, so it can't all be tested until you've completed the whole problem set. There are tests for later problems that rely upon this working correctly.

CACHE_FNAME = "pset8_cached_data.json" # PROVIDED FOR YOU, DO NOT CHANGE

# Begin a try/except statement. Inside the try block:

## Open a file with the CACHE_FNAME file name.

## Read the file into one big string.

## Load the string into a Python object, saved in a variable called CACHE_DICTION.

# Begin the except clause of the try/except statement:

## Create a variable called CACHE_DICTION and give it the value of an empty dictionary.

# (In total, this should be five or six lines of code. It can be a 1:1 comment:line of code relationship.)



## [PROBLEM 6]
print("\n***** PROBLEM 6 *****\n")

### Utility function definition provided for your use here (DO NOT CHANGE)
## Function to create a unique representation of each request without private data like API keys
def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

## Now,
## DEFINE A FUNCTION called get_flickr_data, which accepts 2 inputs:
## - a REQUIRED parameter: any string representing a tag to search for on Flickr (e.g. if you wanted to search for data on photos tagged with "mountains", you would pass in "mountains" for this parameter)
## - an OPTIONAL parameter whose default value is 50 (representing how many photos you want in your response data)

## The RETURN VALUE of the function should be a Python dictionary representing a bunch of search data from the Flickr Photos Search API.

## The following is an extended description of what the function you're defining in this problem should do.

## FUNCTION BEHAVIOR:
## This function should use the provided utility function called params_unique_combination to get a unique identifier for this particular data request to the Flickr API (searching for this tag phrase and this number of photos).

## This function should check whether or not the unique identifier for each request exists in your cache data, and if it does, should access the Python object that represents that data from the CACHE_DICTION.

## BUT if there is no such data in your cache, the function should make a request to the Flickr Photos Search API for photos tagged with your input string.

## Your request should use the tag_mode "all" so that if your query string represents multiple tags, it will search for photos with ALL of those tags. (Check out the examples from class!)

## It should then modify the string that is returned from the Flickr API so that it is properly JSON formatted. (You want a version of the string without the first 14 characters and without the very last character -- see the textbook example!)

## And then, load that modified string into a Python object. The function should add the new dictionary of data to your cache dictionary, associated with the unique identifier key, and should write ALL the data in the cache dictionary, now with an additional key-value pair, to your cache file!

## RETURN VALUE: The get_flickr_data function's return value, regardless of whether it got data from the cache or made a new request and saved data to the cache, should be a big dictionary representing a bunch of search data from the Flickr Photos Search API.

## API docs here for that API endpoint: flickr.com/services/api/flickr.photos.search.html

## The base URL for the Flickr API is: "https://api.flickr.com/services/rest/"

## Recall that all Flickr API endpoints have the same base url, but different values of the "method" parameter! For the Photos Search API, that value should be "flickr.photos.search"

## Recall also that you have a variable FLICKR_KEY in this file which you could reuse in this function, since it is intended as a global variable for your whole program.


## Referring to the examples from class and from the textbook  about caching, and talking through them carefully, will be VERY helpful here. The work you did in Problem Set 7 may also be a helpful reference, though remember that the functions you wrote in PS7 did NOT cache any data in this manner, and the flickr API requires more query parameters than the FAA API does!

## There are tests for this problem, and the autograde script will run an additional test (invoking the function with new input to see if the caching works correctly!).





## [PROBLEM 7]
print("\n***** PROBLEM 7 *****\n")

## Make an invocation to your get_flickr_data function with the input "mountains" (use the default second parameter). Save the result in the variable flickr_mountains_result. There are tests for this problem.

## (Whether or not this works is also an additional test for your Problem 6, since this won't work without the get_flickr_data function you defined above.)


## [PROBLEM 8]
print("\n***** PROBLEM 8 *****\n")

## Remember the code you wrote in Problem 4? Refer to that code, and now, write code to get a list of all of the photo IDs in the data that's in your flickr_mountains_result variable.
## Save that list in a variable called photo_ids.
## There are tests for this problem.




## [PROBLEM 9]
print("\n***** PROBLEM 9 *****\n")
## Finally, you'll use what you know to define a function that makes a different request: a request to the Flickr API endpoint for Photo Information ("getInfo", it's called).
## Documentation for that API endpoint is here: https://www.flickr.com/services/api/flickr.photos.getInfo.html
## The baseurl for this endpoint is the same as for the other Flickr API endpoint you already used in Problem 6!

## For this problem, define a function called get_photo_data_with_caching that takes as input only 1 photo ID.
## Just like in Problem 6, your function should make a request to an API endpoint from Flickr, and return data in Python object form.
## This function should also CACHE data -- again, just like Problem 6.
## The differences between this function and the function in Problem 6 are as follows.
## - Different input: This function should accept only 1 required parameter -- a string that contains 1 valid photo id.
## - Different value of the method parameter, so you make a request to the correct API endpoint
## - Different parameters: this endpoint requires only the api key parameter, and the photo id parameter
## Everything else is pretty much the same.

# Code to define your get_photo_data_with_caching function here...



## Tests for this problem simply test if you have written this function correctly, but I recommend you try it out: invoke it with the first photo id from your photo search data!

# You could write a sample invocation to that function here.


## [CHALLENGE]
print("*** CHALLENGE (optional) ***\n")

## Continuing from this, you can write code to build a tag recommender: given a search for a certain tag on Flickr, your code could tell you 5 other tags which most frequently co-occur with the tag you searched for.

## We will be looking at or building code to do this in the future, but if you're looking for a challenge, try writing it now! (We will not offer extra credit for this at this point, but it's a good idea to try it out, or if not, try thinking about it: what would your plan be to do this, in English?)

## Hint: It will be useful to make requests to the Photo Info endpoint of the Flickr API
## Hint 2: It will be useful to make a dictionary of all of the tags... and to do a bit of sorting.

## MAKE SURE that if you write the code inside this file, it does not keep your file from running, though!
## We have NOT provided tests for this yet.
