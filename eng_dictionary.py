import json
from difflib import get_close_matches

data = json.load(open("data.json"))  # data.json contains the dictionary information


def translate(w):  # returns a list of stings (definitions) for the words that have a match or an informational
    # message (sting)
    if w.lower() in data.keys():
        return data[w.lower()]
    elif w.title() in data.keys():  # handles cases such as: Central Africa, Italy, etc
        return data[w.title()]
    elif w.upper() in data.keys():  # handles cases such as: USA, NATO, etc
        return data[w.upper()]
    elif get_close_matches(w, data.keys(), n=1, cutoff=0.8):  # pythonic implicit booleanness
        yn = input("Did you mean {} instead? Enter Y if yes, or N if no: ".format(get_close_matches(w, data.keys(), n=1,
                                                                                                    cutoff=0.8)[0]))
        if yn.lower() == "y":
            return data[get_close_matches(w, data.keys(), n=1, cutoff=0.8)[0]]  # return the closest match in case of
            # user input mistype
        elif yn.lower() == "n":
            return "Sorry for asking."
        else:
            return "You didn't enter Y or N."
    else:
        return "The word doesn't exist. Please double check it."


while True:
    word = input("Enter word: ")
    if word == "\\quit":
        print("Thank you for using the dictionary.")
        break
    else:
        output = translate(word)
        if isinstance(output, list):
            i = 1
            for item in output:
                print("{}) {}".format(i, item))
                i += 1
        else:
            print(output)
