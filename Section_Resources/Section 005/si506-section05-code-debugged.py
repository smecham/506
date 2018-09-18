# SI 506 - Programming I

# Import statements (do not change)
import unittest

# Definitions taken from dictionary.com
# Consulted: 2018



d1 = {
		"help":"to give or provide what is necessary to accomplish a task or satisfy a need; contribute strength or means to; render assistance to; cooperate effectively with; aid; assist",
		"find":"to come upon by chance; meet with",
		"produce":"to bring into existence; give rise to; cause",
		"extract":"to get, pull, or draw out, usually with special effort, skill, or force",
		"verify":"to prove the truth of, as by evidence or testimony; confirm"
}

d2 = {
		"providence":"the foreseeing care and guidance of God or nature over the creatures of the earth.",
		"happenstance":"a chance happening or event.",
		"milestone":"a stone functioning as a milepost.",
		"turnout":"the gathering of many persons who come to an exhibition, party, spectacle, or the like",
		"potty":"slightly insane; eccentric."
		}

quotes = {
		"help":"He planned to help me with my work. Let me help you with those packages.",
		"find":"He found a nickel in the street.",
		"produce":"to produce steam.",
		"verify":"Events verified his prediction."
		}

# BUG 1: d3 does not exist. Try the quotes dictionary
examplelist = list(quotes.keys()) # Not a list if we don't do this casting
for k in examplelist:
	if len(k) % 2 == 0:
		print(k)

def longestdefinition(definitiondiction):
	keys = list(definitiondiction.keys())
	longest = keys[0]
	for k in keys[1:]:
		if len(definitiondiction[k]) > len(definitiondiction[longest]):
			longest = k
	# BUG 2: longest should be outside of the loop
	return longest

longest_defn = longestdefinition(d1)

longest_other_defn = longestdefinition(d2)


def get_example_spec(dictofexamples={"hello":"greeting"}, word="hello"): # BUG 3: missing column
	if word in dictofexamples:
		#print(dictofexamples[word]) # BUG 4: code was only printing and then returning NONE
		return dictofexamples[word]
	else:
		#print("Nope")
		return "Nope" # BUG 5: function was only printing and then returning NONE

print("="*30)

print(get_example_spec()) # SHOULD print: greeting [and should print nothing else]
						  # BUG 6: Function call was missing parenthesis in line above

print(get_example_spec()) # SHOULD print: greeting [and should print nothing else]

print("="*30)

res = get_example_spec(d2, "turnout")

separate = get_example_spec(quotes, "experience") # Many ways to fix this line...
												  # BUG 7: I substituted the first parameter with the quotes dictionary
another = get_example_spec(quotes, "found") # Don't change the dictionary itself to fix this
											# NOTE: bugs were not in the line, but in the function definition



##### Testing code below this line.
##### Do not change.

if __name__ == "__main__":

	class TestSampleCode(unittest.TestCase):
		def test_definitions_ex(self):
			self.assertEqual(longest_defn, "help")
		def test_definitions_2(self):
			self.assertEqual(longest_other_defn, "turnout")

	class TestSampleCodeSecond(unittest.TestCase):
		def test_res(self):
			self.assertEqual(res,"the gathering of many persons who come to an exhibition, party, spectacle, or the like")
		def test_fxn1(self):
			self.assertEqual(get_example_spec(), "greeting")
		def test_fxn2(self):
			self.assertEqual(get_example_spec(word="goodbye"),"Nope")
		def test_fxn3(self):
			self.assertEqual(get_example_spec({"1":12,"3":45},"3"),45)
		def test_another(self):
			self.assertEqual(another, "Nope")
		def test_fxn4(self):
			self.assertIsInstance(get_example_spec(),str)

	unittest.main(verbosity=2)