import requests
import json

#   Get an OMDb API Key from: http://www.omdbapi.com/apikey.aspx
OMDB_API_KEY = '3207b433' # 1000 daily limit for free one

#   Define a function getOMDBData that accepts a title and calls the OMDb API (described here: http://www.omdbapi.com) to get the data about that movie. Use the data request API endpoint, and  refer to the "By ID or Title" features of the OMDb API (not the "By Search" features)

# Requirements:
#   If the user enters an invalid title, your function should return the *boolean* False. Note that when the title is invalid, OMDb sends back data where the 'Response' field is set to 'False' (a string)
#   Only use TWO URL parameters (one for the title and one for the API key)

def getOMDBData(title):
        info=requests.get('http://www.omdbapi.com/?apikey=3207b433', params={'t': title})
        movie_str=info.text
        movie_py=json.loads(movie_str)

        if movie_py['Response'] == 'False':
            return(False)
        else:
            return(movie_py)

practice_run= getOMDBData('Titanic')
print(practice_run)

practice_error= getOMDBData('ThisIsGibberish')
print(practice_error)
print(type(practice_error)) #Should be boolean

#   Function getMoviesData that accepts a *list* of titles (strings) and returns a *list* of dictionaries fetched from the OMDb API

def getMoviesData(movieTitles):
    list_of_dicts=[]
    for each_title in movieTitles:
        movie_dict=getOMDBData(each_title)
        list_of_dicts.append(movie_dict)
    return(list_of_dicts)

movies_to_see = ['Nightmare On Elm Street', 'The Shining', 'It', 'Psycho']
movie_data=getMoviesData(movies_to_see)
print(movie_data)

one_is_fake= ['Scream', 'The Cabin in the Woods', 'Blingelblorgen', 'The Blair Witch Project']
fake_data=getMoviesData(one_is_fake)
print(fake_data)


#   Function getValidMoviesData that accepts a list of movie titles and returns a list of dictionries fetched from the OMDb API but only for valid movie names.

def getValidMoviesData(movieTitles):
    get_data= getMoviesData(movieTitles)
    while False in get_data: get_data.remove(False)
    return (get_data)

one_is_fake= ['Scream', 'The Cabin in the Woods', 'Blingelblorgen', 'The Blair Witch Project']
fake_data=getValidMoviesData(one_is_fake)
print(fake_data)

all_are_fake= ['Stephanie Mecham', 'Goes to U of M']
more_fake_data=getValidMoviesData(all_are_fake)
print(more_fake_data)

#   Function sortedMoviesData that accepts a *list* of movie titles and returns a list of dictionres fetched from the OMDb API that are sorted by their IMDB ratings *from high to low*. Only include valid movies.

def sortedMoviesData(movieTitles):
    movies_data= getValidMoviesData(movieTitles)
    for each_title in movies_data:
        float(each_title['imdbRating'])
    sorted_movies_data=sorted(movies_data, key=lambda x: x['imdbRating'], reverse=True)
    return(sorted_movies_data)

list_of_movies= ["Poltergeist", "Halloween", "Friday the 13th", "Rosemary's Baby"]
sort_by_ratings=sortedMoviesData(list_of_movies)
print(sort_by_ratings)

testing_fakes_again= ["This Is Not a Real Horror Movie", "The Ring", "The Exorcist"]
sort_by_imdb=sortedMoviesData(testing_fakes_again)
print(sort_by_imdb)

#Keep track of a list of movies that the user has viewed in the file viewed_movies.txt

PREVIOUSLY_VIEWED_FNAME = 'viewed_movies.txt'

try:
    open_file= open(PREVIOUSLY_VIEWED_FNAME, 'r')
    read_data= open_file.read()
    open_file.close()
    viewed_movies= json.loads(read_data)
except:
    viewed_movies=[]

print(viewed_movies)

#   Function hasSeenMovie that accepts a title and returns the boolean True if that title is an item in viewed_movies and the boolean False otherwise

def hasSeenMovie(title):
    if title in viewed_movies:
        return True
    else:
        return False

have_you_watched= hasSeenMovie('Cloverfield')
print(have_you_watched)

#  Function markAsViewed that accepts a title, and:
#       - If that title IS in viewed_movies, do nothing
#       - If that title IS NOT in viewed_movies, add it to the list and then open up the PREVIOUSLY_VIEWED_FNAME file for writing. Then write the contents of the viewed_movies variable to the file PREVIOUSLY_VIEWED_FNAME
#       - The function should always return None

def markAsViewed(title):
    if hasSeenMovie(title) == True:
        pass
    elif hasSeenMovie(title) == False:
        viewed_movies.append(title)
        json_version= json.dumps(viewed_movies)
        movie_file=open(PREVIOUSLY_VIEWED_FNAME, 'w')
        movie_file.write(json_version)
        movie_file.close()
    return(viewed_movies)

haha= markAsViewed("Real Steel")
print(haha)

have_watched= markAsViewed("Silence of the Lambs")
print(have_watched)

do_it_again= markAsViewed("Real Steel")
print(do_it_again)

#   Function getMovieAdvice that takes zero input arguments and proceeds through the following steps:
#   1) Ask the user for a list of movies separated by commas (no spaces -- e.g. --> Titanic,The Big Chill,Black Panther)
#   2) Split by commas to create a list of strings that represent movie titles
#   3) Call the sortedMoviesData function on that list of movie titles, and save the return value in a variable.
#   3) Loop over each movie in the resulting list variable. For each movie:
#    3-1): If the user has seen the movie before, print the following:
#               "You have already seen {title}""
#    3-2): If the user has NOT seen the movie before, print out the movie title, year, IMDB rating, and plot in the format:
#
#               {title} ({year}): {IMDB rating}
#               --------------------
#               {plot}
#
#           For example:
#               The Big Chill (1983): 7.2
#               --------------------
#               A group of seven former college friends gather for a weekend reunion at a South Carolina winter house after the funeral of one of their friends.
#
#     3-3): Then, still in the function body, ask the user if they want to watch the movie (yes or no)
#         If the user types "no" (or anything other than "yes") do nothing. If the user types "yes", then call markAsViewed on that movie title. **Note:** you should use the 'Title' supplied by OMDb (not necessarily what the user initially entered).
#         Then, print the runtime in the following format:
#
#               Watched {title} for {runtime}
#
#         For example:
#
#               Watched The Big Chill for 105 min

def getMovieAdvice():
    movies= input("Enter a list of movies, separated by commas and with no spaces here:")
    movies_separate= movies.split(',')
    sorted_movies= sortedMoviesData(movies_separate)

    for each_movie in sorted_movies:
        seen_before= hasSeenMovie(each_movie['Title'])
        if seen_before == True:
            print("You have already seen " + each_movie['Title'])
        else:
                print('\n' + each_movie['Title'] + '('+each_movie['Year']+'):' + each_movie['imdbRating'] + '\n' + '--------------------' + '\n' + each_movie['Plot'] + '\n')
                want_to_watch= input("Would you like to watch " + each_movie['Title'] + "- yes or no?")
                if want_to_watch != 'yes':
                    pass
                else:
                    will_watch= markAsViewed(each_movie['Title'])
                    print('\n' + 'Watched ' + each_movie['Title'] + ' for ' + each_movie['Runtime'])
    return (sorted_movies)


trial= getMovieAdvice()

if __name__ == "__main__":
    getMovieAdvice()
