import json


print("\n*** PROBLEM 1 ***\n")

f= open("nested_data_ps6.json", "r")
read_file= f.read()
file_diction = json.loads(read_file)
print(file_diction)

print("\n*** PROBLEM 2 ***\n")

python_diction = {}
python_diction["items"] = []
python_diction["items"].append({"hello":1,"hi":2})
python_diction["items"].append({"hello":42,"hi":65})
python_diction["numbers"] = [1,2,3,5,7,8]

dumped_data= json.dumps(python_diction)
outfile= open("python_diction_saved.json" , "w")
outfile.write(dumped_data)
outfile.close()

print("\n*** PROBLEM 3 ***\n")

## itunes_data.json: contains data from iTunes API that results from a search for the artist Solange.

open_file = open("itunes_data.json", "r")
read_data = open_file.read()
solange = json.loads(read_data)
print(type(solange))

song_titles=[]
result_data= solange["results"]
for data in result_data:
    title=data["trackName"]
    song_titles.append(title)
print(song_titles)

first_listing = result_data[0]
first_album = first_listing["collectionName"]
print(first_album)


album_titles= []
for data in result_data:
    album= data["collectionName"]
    album_titles.append(album)
print(album_titles)

longest_song = result_data[0]
for data in result_data:
    if data["trackTimeMillis"] > longest_song["trackTimeMillis"]:
        longest_song = data
print(longest_song)

## Generate a list of the strings representing each of the UNIQUE genres among the songs in this data.

unique_genres=[]
for data in result_data:
    genre=data["primaryGenreName"]
    if genre not in unique_genres:
        unique_genres.append(genre)
print(unique_genres)

print("\n*** PROBLEM 4 ***\n")

def numbers_stuff(inp):
    res = 26 + inp*3
    res += 4
    return res/inp

to_input = int(input("What number to put in?"))

try:
    print(numbers_stuff(to_input))
except ZeroDivisionError:
    print("Sorry, you cannot input 0 to this function")
