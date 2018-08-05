'''
a script,
that takes a word as input,
if user misspell the word ,it suggest the most probable word and prints the defination of the word
 
'''
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	
	if word in data:
		return data[word]
	elif len(get_close_matches(word , data.keys()))>0:
		print("Did you mean %s instead?" % get_close_matches(word , data.keys())[0])
		yn = input(" Enter Y if yes or N if no \n")
		yn = yn.lower()
		if yn == 'y':
			return data[get_close_matches(word , data.keys())[0]]
		elif yn == 'n':
			return "The word doesn't exist, please double check it"
		else:
			return "We didn't understand your query"
	else:
		return "The word doesn't exist, please double check it"


word = input("Enter any word \n")
w = translate(word)
if type(w)==str:
	print(w)
else:
	c= 1
	for i in w:
		print("%d" %c,end='.')
		print(i)
		c = c+1

