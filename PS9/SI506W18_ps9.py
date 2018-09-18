import json
import unittest
import random

## [PROBLEM 1]
print("\n\n***** Problem 1 *****")

class Photo(object):
    def __init__(self, title_str, photo_by, tags_list):
        self.title = title_str
        self.artist = photo_by
        self.tags = tags_list

    def __str__(self):
        return "{} by {}".format(self.title,self.artist)


single_photo= Photo('Photo1','Ansel Adams',['river','yosemite'])
print(single_photo)

## [PROBLEM 2]
print ("\n\n***** Problem 2 *****")

tups_list = [("Portrait 2","Gordon Parks",["chicago", "society"]),("Children in School","Dorothea Lange",["children","school","1930s"]),("Airplanes","Margaret Bourke-White",["war","sky","landscape"])]

photo_insts=[]
for each_tuple in tups_list:
    (title_str, photo_by, tags_list)=each_tuple
    photo_insts.append(Photo(title_str, photo_by, tags_list))

for i in photo_insts:
    print(i)

## [PROBLEM 3]
print ("\n\n***** Problem 3 *****")

class Student(object):
    def __init__(self, name, years_at_umich=1):
        self.name = name
        self.years_UM = years_at_umich
        self.bonus_points = random.randrange(1000)
        self.programs_written = 0

    def shout(self, phrase_to_shout):
        print(phrase_to_shout)

    def year_at_umich(self):
        return self.years_UM

    def __str__(self):
        return("My name is " + self.name + ". I've been at UMich for " + str(self.years_UM) + " years and I've written " + str(self.programs_written) + " programs.")

    def write_programs(self, progs=1):
        self.programs_written = self.programs_written + progs

s = Student("Lyra")
print (s) #Should print: My name is Lyra. I've been at UMich for 1 years and I've written 0 programs.
s.shout("I'm doing awesome on this problem set") # Should result in this printing: I'm doing awesome on this problem set
print (s.year_at_umich()) # Should print 1
s.write_programs()
print(s.programs_written) # Should print 1
s.write_programs(6)
print(s.programs_written) # Should print 7
print(s) # Should print: My name is Lyra. I've been at UMich for 1 years and I've written 7 programs.
s.write_programs(progs=4)
print(s) # Should print: My name is Lyra. I've been at UMich for 1 years and I've written 11 programs.

## [PROBLEM 4]
print ("\n\n***** Problem 4 *****")

class Apple(object):
    def __init__(self, color, variety_name, size, place_grown):
        self.color = color
        self.variety= variety_name
        self.size = size
        self.grown_in = place_grown

    def for_pies(self):
            if self.variety in ["Granny Smith", "Braeburn", "Golden Delicious"]:
                return True
            else:
                return False

    def __str__(self):
            return("A " + self.size + " " + self.color + " apple of the " + self.variety + " variety, grown in " + self.grown_in + ".")


ap = Apple("red","Braeburn","medium","WA")
print(ap) # Should print: A medium red apple of the Braeburn variety, grown in WA.

ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
print(ap2) # Should print: A large green apple of the Granny Smith variety, grown in Sydney, Australia.
print(ap2.for_pies()) # should print True

ap3 = Apple("red","Mystery", "small","Michigan")
print(ap3.for_pies()) # should print False
print(ap3) # should print: A small red apple of the Mystery variety, grown in Michigan.


## [PROBLEM 5]
print ("\n\n***** Problem 5 *****")

class Car(object):
    def __init__(self, color, make, miles_per_gallon):
        self.color = color
        self.make = make
        self.mpg = miles_per_gallon

    def __str__(self):
        return "{} {} car with {} MPG".format(self.color,self.make, self.mpg)

    def miles_can_go(self, gallons_in_tank):
        return float(gallons_in_tank)*self.mpg

c = Car("grey","SUV",20)
print (c.miles_can_go(4)) # Should print: 80.0
print (c) # Should print: grey SUV car with 20 MPG

another_car = Car("rainbow","convertible", 28)
print(another_car) # Should print: rainbow convertible car with 28 MPG
print(another_car.miles_can_go(10)) # Should print: 280.0

## [PROBLEM 6]
print ("\n\n***** Problem 6 *****")

f = open("nested_data_tweet.json",'r')
file_contents = f.read()
f.close()
tweet_diction1 = json.loads(file_contents)

class Tweet(object):
    def __init__(self, tweet_diction1):
        self.text = tweet_diction1["text"]
        self.user = tweet_diction1["user"]["screen_name"]

    def num_words_text(self):
        return len(self.text.split())
