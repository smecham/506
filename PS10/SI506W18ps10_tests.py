import unittest
from SI506W18_ps10 import *

class Problem1(unittest.TestCase):
    print("No tests for Problem 1 -- it's investigation of the tools you have to use\n")

class Problem2(unittest.TestCase):
    def test_twitter_music_data(self):
        self.assertIsInstance(twitter_music_data, dict)
    def test_twitter_music_data2(self):
        self.assertEqual(sorted(list(twitter_music_data.keys())),['search_metadata', 'statuses'],"Testing the keys in the data retrieved from Twitter")
    def test_twitter_music_data3(self):
        self.assertEqual(len(twitter_music_data["statuses"]),50,"Testing that there are 50 tweets in the data") # Should be 50 tweets

class Problem3(unittest.TestCase):
    def setUp(self):
        f = open("sample_tweet.json")
        fstr = f.read()
        f.close()
        self.twitterdiction = json.loads(fstr)
    def test_fav_count(self):
        inst = Tweet(self.twitterdiction)
        self.assertEqual(inst.favs, 27, "Testing the number of favs is accessed correctly in self.favs")
    def test_text(self):
        inst = Tweet(self.twitterdiction)
        self.assertEqual(inst.text, "COMING UP TODAY AT 5 on the @zachsang1 #WorldWideCountdown, music from @taylorswift13, @Migos, @JaxJones, https://t.co/uaBNthFWNv")
    def test_hashtags(self):
        inst = Tweet(self.twitterdiction)
        self.assertEqual(inst.hashtags,['WorldWideCountdown'])
    def test_hashtags2(self):
        inst = Tweet(self.twitterdiction)
        self.assertIsInstance(inst.hashtags,list,"Testing that the hashtags instance var is type list")
    def test_username(self):
        inst = Tweet(self.twitterdiction)
        self.assertEqual(inst.username,"kiss1031")

class Problem4(unittest.TestCase):
    def test_tweet_insts(self):
        self.assertIsInstance(tweet_insts,list,"Testing that tweet_insts is a list")
    def test_tweet_insts2(self):
        self.assertEqual(len(tweet_insts),50,"Testing that there are 50 instances in the list")
    def test_tweet_insts3(self):
        self.assertTrue(tweet_insts[0].text,"Testing the first element of the list has a text attr like a Tweet inst should")
        self.assertTrue(tweet_insts[-1].username, "Testing the last element of the list has a text attr like a Tweet inst should")
    def test_tweet_insts4(self):
        self.assertTrue(tweet_insts[0] != tweet_insts[25], "Testing there are different tweets in the list of tweet instances")

class Problem5(unittest.TestCase):
    def test_file_exists(self):
        fileref = open("tweet_info.csv")
        self.assertTrue(fileref.read(),"Testing you can open the CSV file to read")
        fileref.close()
    def test_file_csv(self):
        fileref = open("tweet_info.csv")
        lines = fileref.readlines()
        fileref.close()
        self.assertTrue(len(lines)>40,"Testing that there are at least 40 lines in the file (accounting for possible errors, maybe no headers)")
        self.assertTrue(len(lines)<=51,"Testing that there are no more than 51 lines meaning newlines are taken care of")
    def test_file_csv_format(self):
        fileref = open("tweet_info.csv")
        lines = fileref.readlines()
        fileref.close()
        self.assertEqual(len(lines[0].split(",")),4,"Testing that each line has the correct number cols")
        self.assertEqual(len(lines[28].split(",")),4,"Testing that each line has the correct number cols")


if __name__ == "__main__":
    unittest.main(verbosity=2)
