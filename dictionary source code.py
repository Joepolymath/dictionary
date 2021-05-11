import json
import difflib
# from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('original.json'))


def diction(word):
    word = word.lower()
    if word in data:
        result = data[word]
        x =1
        y=0
        for w in result:
            print (str(x) + "." + result[y])
            x+=1
            y+=1

    elif len(get_close_matches(word, data.keys())) > 0:
        print("Do you mean %s instead?" % get_close_matches(word, data.keys())[0])
        check = input("type 'y' if yes. type 'n' for no:   ")
        check = check.lower()
        if check == 'y':
            result = data[get_close_matches(word, data.keys())[0]]
            
        elif check == 'n':

            result = "sorry word does not exist"
        else:
            result = "Wrong entry"

    else:
        result = "word does not exist"
    return result

while True:

    word = input("Enter your word:   ")
    if word == '/end':
        break
    diction(word)
    
