import unittest
import json
from SI506W18_ps7 import *

print('NOTE: Passing these tests does *not* ensure that your code works properly')

class PS08Tests(unittest.TestCase):
    def test_problem01(self):
        tbc_example = getOMDBData("The Big Chill")
        self.assertTrue('Title' in tbc_example, 'Checking that has title')
        self.assertTrue('Runtime' in tbc_example, 'Checking that has runtime')
        self.assertTrue('imdbRating' in tbc_example, 'Checking that has IMDB rating')
        self.assertTrue('Plot' in tbc_example, 'Checking that has plot')

        invalid_example = getOMDBData("asdfasdfasdfasdfasdf")
        self.assertFalse(invalid_example, 'Checking that False is returned for invalid movies')
    def test_problem02(self):
        examples = getMoviesData(["The Big Chill", "asdfasdfasdfasdfasdf"])
        self.assertEqual(len(examples), 2)
        self.assertEqual(type(examples[0]), type({}))
        self.assertFalse(examples[1])
    def test_problem03(self):
        examples = getValidMoviesData(["The Big Chill", "asdfasdfasdfasdfasdf"])
        self.assertEqual(len(examples), 1)
        self.assertEqual(type(examples[0]), type({}))
    def test_problem04(self):
        examples = sortedMoviesData(["Superbabies: Baby Geniuses 2", "The Shawshank Redemption", "asdfasdfasdfasdfasdf" , "Source Code"])
        self.assertEqual(len(examples), 3)
        self.assertEqual([m['Title'] for m in examples], ['The Shawshank Redemption', 'Source Code', 'Superbabies: Baby Geniuses 2'])
    def test_problem050607(self):
        print('(no tests for problems 5, 6, 7, or 8)')

if __name__ == "__main__":
    unittest.main(verbosity=2)
