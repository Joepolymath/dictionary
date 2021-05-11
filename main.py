import json
data = json.load(open('original.json')

def diction(word):
	result = data[word]
	return result

word = input("enter your word:  ")
print(diction(word))