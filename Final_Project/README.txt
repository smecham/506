{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf400
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww12600\viewh10980\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 SI 506 Final Project  |  README  |  Stephanie Mecham  |\
\
\
* In ~2-3 sentences, what does your project do?\
\
If you put your personal consumer key, consumer secret, access token, and access token secret into the twitter_info.py file and run the program, this code will allow you to search Twitter by a keyword of your choosing, and will request songs from the iTunes API based on the longest words from the tweets that your search generated. Data about these tweets and the songs corresponding to their longest words will be output into a playlist in a CSV file format.\
\
* What files (by name) are included in your submission?\
\
Included files and their contents:\
SI506W18_final_project.py \'97> code containing the technical requirements for the program to run\
twitter_info.py \'97> contains the information for my Twitter account, in order to make requests to the Twitter API\
SI506W18final_project_cache.json \'97> cached data from my Twitter API and iTunes API search requests\
Sample Output.jpg \'97> Screenshot of what CSV output should look like when program is run\
Program Running 1.jpg \'97> Screenshot of what program looks like when I run it\
Program Running 2.jpg  \'97> Screenshot of what program looks like when I run it (too long to fit on one screenshot)\
README.txt \'97> This document!\
\
\
* What Python modules must be pip installed in order to run your submission? List them ALL (e.g. including requests, requests_oauthlib... anything someone running it will need!). Note that your project must run in Python 3.\
\
Install the following Python modules with pip:\
requests\
requests_oauthlib\
\
The following Python modules need to be imported but are part of the Python Standard Library:\
webbrowser\
json\
csv\
\
\
* Explain SPECIFICALLY how to run your code. \
\
After putting your personal Twitter information into the corresponding fields in the twitter_info.py file (this includes a consumer secret and access token secret), run the SI506W18_final_project.py file.  A prompt will appear asking you to enter a search term. An example you can try is \'93lake\'94. Each Tweet instance and Song instance pulled from the Twitter or iTunes API or the cache dictionary will be printed to the console in the format specified in their respective __str__ methods. The console will tell you whether each instance was pulled from the API directly or from the cache (by printing \'93Retrieving cached data\'85\'94 if pulling from the cache or printing \'93Making request to the (Twitter/iTunes) API\'85\'94 if the request is not already located in the cache. In some cases, a word used for a request to the iTunes API will not generate any song matches (for example, if the longest word of a tweet is gibberish or something uncommon). In this case, the console will print \'93There is no iTunes song for that word!\'94.  \
\
Searches can contain spaces, commas, apostrophes, and other special ASCII characters. However, searches that are too long (longer than a few words) likely won\'92t be able to generate any data. For example, the search \'93Don\'92t Stop Til You Get Enough\'94 will generate results, but \'93Don\'92t Stop Til You Get Enough, Ya Filthy Animal\'94 will not.\
\
\
* Where can we find all of the project technical requirements in your code? Fill in with the requirements list below.\
\
REQUIREMENTS LIST:\
Line numbers below all refer to the SI506W18_final_project.py file, unless otherwise specified. \
\
* Get and cache data from 2 REST APIs (list the lines where the functions to get & cache data begin and where they are invoked):\
Cache dictionary set-up function is located on lines 13-21.\
Caching data for the Twitter API authorization is located on lines 52-61.\
The function for making requests to the cache or the Twitter API is located on lines 73-97. \
The function for making requests to the cache or the iTunes API is located on lines 106-130. \
\
* Define at least 2 classes, each of which fulfill the listed requirements (see requirements sheet):\
The definition for the Tweet class begins on line 137.\
The definition for the Song class beings on line 189.\
\
* Create at least 1 instance of each class:\
Creating Tweet instances occurs at line 208. \
Creating Song instances occurs at line 227.\
\
* Invoke the methods of the classes on class instances:\
Invoking methods for Tweet instances occurs on lines 185/216-219. \
Invoking methods for Song instances occurs on lines 201/232-233.\
\
* At least one sort with a key parameter:\
Sorting the list of Tweet instances by number of hashtags occurs on line 216.\
\
* Define at least 2 functions outside a class (list the lines where function definitions begin):\
get_tokens function begins on line 30.\
params_unique_combination begins on line 63.\
get_from_twitter begins on line 73.\
get_from_itunes begins on line 106.\
\
* Invocations of functions you define:\
Invocation of get_tokens occurs on line 55.\
Invocation of params_unique_combination occurs on line 79 and 113.\
Invocation of get_from_twitter occurs on line 102.\
Invocation of get_from_itunes occurs on line 225.\
\
\
* Create a readable file:\
The writing to a CSV file portion begins on line 241. \
\
END REQUIREMENTS LIST\
\
* Citations\
\
I used code from SI 506 Problem Set 10 for the caching pattern, get_tokens function, and params_unique_combination function. I used code from SI 506 Problem Set 9 for reference on how to make API requests, and on creating classes. I referenced the textbook section on list comprehension and an answer on Stack Overflow provided by user \'91utdemir\'92 ({\field{\*\fldinst{HYPERLINK "https://stackoverflow.com/questions/6930479/any-way-to-zip-to-list-of-lists"}}{\fldrslt https://stackoverflow.com/questions/6930479/any-way-to-zip-to-list-of-lists}}) to help me create line 237. I used the Python 3 documentation for the CSV module to help write my CSV file (link: {\field{\*\fldinst{HYPERLINK "https://docs.python.org/3/library/csv.html"}}{\fldrslt https://docs.python.org/3/library/csv.html}}).\
\
* Explain in a couple sentences what should happen as a RESULT of your code running: what CSV or text file will it create? What information does it contain? What should we expect from it in terms of approximately how many lines, how many columns, which headers...?\
\
A CSV file called \'91tweets_songs.csv\'92 should appear in your working directory. It will contain a title row with the project title and my name. It will contain a header row labeling the columns about what aspect of data about the Tweet or Song instances you are looking at. The maximum number of lines will be 100 (or whatever you set as the parameter for how many tweets the program should output. This parameter can be changed on line 102). If there are much fewer rows than that, try a more common search term. \
\
* Is there anything else we need to know or that you want us to know about your project? Include that here!\
\
Note 1) For rarer keyword searches, the playlist that is output likely would consist of many repeats \'97 songs and tweets referencing the same original tweet that has just been retweeted multiple times. Because of this, I decided to exempt retweets from this program. The code for this occurs on line 207.\
\
Note 2) The function that finds the longest word of each tweet does not take ties into account ties. Therefore, if there are multiple words in a Tweet that have the same length, the longest word the function return is simply the one that appears last in the Tweet (the last one to go through the for loop and replace the best-so-far word of the same length). This is a limitation that has not been addressed in this project due to the fact that I wanted only one iTunes search per tweet, even if there were multiple different \'93longest words\'94 in that tweet.\
\
Note 3) I did not want any URL links or Twitter usernames to be counted as contenders for the longest word. Therefore, I excluded words that began with \'91http\'92 or \'91@\'91 from the longest word function, and had the console print \'93Do nothing\'94 when words that met those conditions were passed through the for loop. That is why you likely see so many \'93Do nothing\'94 statements when running the program. The code for this portion is located on lines 156-159.}