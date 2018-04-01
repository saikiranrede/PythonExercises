import json
import difflib

from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def meaning(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8))>0:
        temp =input("Did you mean %s ? Y or N: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if temp == "Y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif temp == "N":
            return "Sorry, we couldn't find a match"
        else:
            return "Sorry, %s is not an option" % temp
    else:
        return "No such word, Please check the word you've entered"
inputWord = input("Enter a word: ")

output = meaning(inputWord)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
