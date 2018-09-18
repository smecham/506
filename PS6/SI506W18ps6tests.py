import unittest
import json
from SI506W18_ps6 import *

class Problem1(unittest.TestCase):
    def setUp(self):
        f = open("nested_data_ps6.json",'r')
        self.filestr = f.read()
        f.close()
        self.diction = json.loads(self.filestr)
    def test_prob2(self):
        self.assertEqual(file_diction,self.diction,"Testing that file_diction has the correct content")

class Problem2(unittest.TestCase):
    def setUp(self):
        f = open("python_diction_saved.json",'r')
        self.file_ref = f
        self.filestr = f.read()
        self.diction = json.loads(self.filestr)
    def test_prob2(self):
        self.assertTrue(self.file_ref,"Testing that the correct file exists")
    def test_prob2_content(self):
        self.assertTrue(len(self.filestr) > 10, "Testing that the string from the file has substantial content")
    def test_prob2_content2(self):
        self.assertIsInstance(self.diction, dict,"Testing that what was saved can be loaded as a dictionary type")
    def tearDown(self):
        f.close()
        self.file_ref.close()

class Problem3(unittest.TestCase):
    def setUp(self):
        fl = open("itunes_data.json",'r')
        self.solange_diction = json.loads(fl.read())
        fl.close()
    def test_p3part1(self):
        self.assertEqual(song_titles,[x["trackName"] for x in self.solange_diction["results"]])
    def test_p3part2(self):
        self.assertEqual(first_album,"A Seat at the Table")
    def test_p3part3(self):
        self.assertEqual(album_titles, [x["collectionName"] for x in self.solange_diction["results"]])
    def test_p3part4(self):
        self.assertEqual(longest_song, {'wrapperType': 'track', 'kind': 'song', 'artistId': 927803, 'collectionId': 1040206681, 'trackId': 1040207081, 'artistName': 'Solange', 'collectionName': 'Sol-Angel & the Hadley St. Dreams (Deluxe)', 'trackName': 'The Bird', 'collectionCensoredName': 'Sol-Angel & the Hadley St. Dreams (Deluxe)', 'trackCensoredName': 'The Bird', 'artistViewUrl': 'https://itunes.apple.com/us/artist/solange/927803?uo=4', 'collectionViewUrl': 'https://itunes.apple.com/us/album/the-bird/1040206681?i=1040207081&uo=4', 'trackViewUrl': 'https://itunes.apple.com/us/album/the-bird/1040206681?i=1040207081&uo=4', 'previewUrl': 'https://audio-ssl.itunes.apple.com/apple-assets-us-std-000001/Music3/v4/34/6d/39/346d3958-3c8a-9132-c623-8724dc7b7dab/mzaf_3942141758974468795.plus.aac.p.m4a', 'artworkUrl30': 'http://is1.mzstatic.com/image/thumb/Music3/v4/6a/33/2c/6a332ce5-c068-0603-1d7e-5be77fa79834/source/30x30bb.jpg', 'artworkUrl60': 'http://is1.mzstatic.com/image/thumb/Music3/v4/6a/33/2c/6a332ce5-c068-0603-1d7e-5be77fa79834/source/60x60bb.jpg', 'artworkUrl100': 'http://is1.mzstatic.com/image/thumb/Music3/v4/6a/33/2c/6a332ce5-c068-0603-1d7e-5be77fa79834/source/100x100bb.jpg', 'collectionPrice': 9.99, 'trackPrice': 0.99, 'releaseDate': '2008-08-26T07:00:00Z', 'collectionExplicitness': 'explicit', 'trackExplicitness': 'notExplicit', 'discCount': 1, 'discNumber': 1, 'trackCount': 17, 'trackNumber': 14, 'trackTimeMillis': 367851, 'country': 'USA', 'currency': 'USD', 'primaryGenreName': 'R&B/Soul', 'isStreamable': True})
    def test_p3part5(self):
        self.assertEqual(sorted(unique_genres),sorted(['R&B/Soul', 'Alternative', 'Soundtrack', 'Pop']))

class Problem4(unittest.TestCase):
    def test_p4_none(self):
        print("\n\n If there are no errors and the correct string from the instructions prints, Problem 4 is solved.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
