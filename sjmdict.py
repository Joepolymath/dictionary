import json
from difflib import get_close_matches

data = json.load(open('original.json'))



def diction(word):
    word = word.lower()
    if word in data:
        meaning = data[word]
        x = 1
        for item in meaning:
            print(str(x) + '.' + ' ' + item)
            x +=1
    elif len(get_close_matches(word, data.keys())) > 0:
        correct = get_close_matches(word, data.keys())[0]
        print("Do you mean %s?" %correct)
        check = input("Type 'y' for yes, and 'n' for no:  ")
        if check=='y':
            meaning = data[correct]
            x = 1
            for item in meaning:
                print(str(x) + '.' + ' ' + item)
                x += 1
        elif check=='n':
            print("Sorry we dont have your word")
        else:
            print("Invalid entry")
    else:
        print("Oga you no understand english")

word = input("ENter your word:   ")
diction(word)