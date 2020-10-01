import argparse
import time
import sys


class AnagramFinder:

	# Function to read the file the dictionary
	def readFile(self):
		list1 = []
		with open(sys.argv[1]) as infile:
			for line in infile:
				line = line.replace('\n','').lower()
				list1.append(line)
			return list1


	#Function to find Anagrams
	def findAnagrams(self, word):
		string_tup = tuple(sorted(word.lower()))
		dict1 = {}
		
		list1 = self.readFile()
		for i in list1:
			key = tuple(sorted(i.lower()))
			
			dict1[key] = dict1.get(key, []) + [i]

		try:
			print(str(len(dict1[string_tup])) + " Anagrams found for " + str(word) + " in %s ms" % round((time.time() - start_time)*100))
			return ",".join(dict1[string_tup])
		except KeyError:
			print("No anagrams found for "+str(word)+" in %s ms" % round((time.time() - start_time)*100))
			return ""
	
	# A switch case function for user to input the desired option	
	def switch(self):
		print("Welcome to the Anagram Finder")
		print("-----------------------------")
		print("Initialized in %s ms" % round((time.time() - start_time)*100)) 
		print("")
		r = str(input("AnagramFinder>"))
		if r == "exit":
			exit()
		else:
			return self.findAnagrams(r)


if __name__ == "__main__":
	start_time = time.time()
	anagram_finder = AnagramFinder()	
	anagram_finder.readFile()
	print(anagram_finder.switch())



'''
TEST CASES:

On command prompt:
python anagram-finder.py dictionary.txt

Input: tutor -> it has two anagrams
Input: arise -> it has for anagrams
Input: pescatarian -> No Anagrams
Input: exit -> exits the program
'''
