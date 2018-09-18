from SI506W18_ps9 import *
import unittest
### DO NOT CHANGE OR REMOVE THIS PRINT LINE! IT IS VERY IMPORTANT FOR GRADING

class Problem1(unittest.TestCase):
    def test_single_photo1(self):
        self.assertEqual(type(single_photo),type(Photo("Photo2","Photo Student",["multiple","tags"])))
    def test_single_photo2(self):
        self.assertEqual(single_photo.title, "Photo1")
    def test_single_photo3(self):
        self.assertEqual(single_photo.artist, "Ansel Adams")
    def test_single_photo4(self):
        self.assertEqual(single_photo.tags, ["river","yosemite"])

class Problem2(unittest.TestCase):
    def test_photo_insts1(self):
        self.assertEqual(type(photo_insts),type([]))
    def test_photo_insts2(self):
        self.assertEqual(type(photo_insts[0]),type(Photo("Photo2","Photo Student",["multiple","tags"])))
    def test_photo_insts3(self):
        self.assertEqual([x.title for x in photo_insts],["Portrait 2", "Children in School", "Airplanes"])
    def test_photo_insts4(self):
        self.assertEqual([x.artist for x in photo_insts],["Gordon Parks","Dorothea Lange","Margaret Bourke-White"])
    def test_photo_insts5(self):
        self.assertEqual([x.tags for x in photo_insts],[["chicago","society"],["children", "school","1930s"],["war","sky","landscape"]])

class Problem3(unittest.TestCase):
    def test_student1(self):
        student1 = Student("Lyra")
        self.assertEqual(student1.__str__(),"My name is Lyra. I've been at UMich for 1 years and I've written 0 programs.")
    def test_student2(self):
        student2 = Student("Aisha")
        student2.write_programs()
        self.assertEqual(student2.__str__(),"My name is Aisha. I've been at UMich for 1 years and I've written 1 programs.")
    def test_student3(self):
        student3 = Student("Ali",3)
        student3.write_programs(4)
        self.assertEqual(student3.__str__(),"My name is Ali. I've been at UMich for 3 years and I've written 4 programs.")
    def test_student4(self):
        student4 = Student("Aja")
        student4.write_programs(12)
        self.assertEqual(student4.programs_written, 12)
        student4.write_programs()
        self.assertEqual(student4.programs_written,13)

class Problem4(unittest.TestCase):
    def test_apple1(self):
        ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
        self.assertEqual(ap2.color,"green")
    def test_apple2(self):
        ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
        self.assertEqual(ap2.variety,"Granny Smith")
    def test_apple3(self):
        ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
        self.assertEqual(ap2.size, "large")
    def test_apple4(self):
        ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
        self.assertEqual(ap2.grown_in, "Sydney, Australia")
    def test_apple5(self):
        ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
        self.assertEqual(ap2.for_pies(),True)
    def test_apple6(self):
        ap2 = Apple("red","Red Delicious","large","WA")
        self.assertEqual(ap2.for_pies(),False)
    def test_apple7(self):
        ap2 = Apple("red","Braeburn","large","WA")
        self.assertEqual(ap2.for_pies(),True)
    def test_apple8(self):
        ap2 = Apple("yellow","Golden Delicious","large","WA")
        self.assertEqual(ap2.for_pies(),True)
    def test_apple9(self):
        ap2 = Apple("yellow","Golden Delicious","large","the United States")
        self.assertEqual(ap2.__str__(), "A large yellow apple of the Golden Delicious variety, grown in the United States.")
    def test_apple10(self):
        ap2 = Apple("red","Braeburn","medium","WA")
        self.assertEqual(ap2.__str__(),"A medium red apple of the Braeburn variety, grown in WA.")

class Problem5(unittest.TestCase):
    def test_car1(self):
        c = Car("grey","SUV",20)
        self.assertEqual(c.__str__(),"grey SUV car with 20 MPG")
    def test_car2(self):
        c = Car("grey","SUV",20)
        self.assertEqual(c.miles_can_go(4), 80.0)
    def test_car3(self):
        c = Car("Blue!!!","convertible",2)
        self.assertEqual(c.__str__(),"Blue!!! convertible car with 2 MPG")
    def test_car4(self):
        c = Car("Blue!!!","convertible",2)
        self.assertEqual(c.miles_can_go(4),8.0)
    def test_car5(self):
        c = Car("Silver","Nissan",26)
        self.assertEqual(c.color, "Silver")
    def test_car6(self):
        c = Car("Silver","Nissan",26)
        self.assertEqual(c.make,"Nissan")
    def test_car7(self):
        c = Car("Silver","Nissan",26)
        self.assertEqual(c.mpg,26)

class Problem6(unittest.TestCase):
    def setUp(self):
        f = open("nested_data_tweet.json",'r')
        self.file_contents = f.read()
        f.close()
        self.tweet_diction = json.loads(self.file_contents)
        self.tweet = Tweet(self.tweet_diction)
    def test_class_tweet1(self):
        self.tweet2 = Tweet(self.tweet_diction)
        self.assertIsInstance(self.tweet2,Tweet)
    def test_class_tweet2(self):
        self.assertEqual(self.tweet.text, "U-M's oldest student group, @UMMGC organized in 1859 and launched a treasured campus tradition. #UMich200 https://t.co/q0koMuRwNo")
    def test_class_tweet3(self):
        self.assertEqual(self.tweet.user, "UMich")
    def test_class_tweet4(self):
        self.assertEqual(self.tweet.num_words_text(),16)


if __name__ == "__main__":
    unittest.main(verbosity=2)
