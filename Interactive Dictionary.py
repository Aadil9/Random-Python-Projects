
#create a function that calls a definition of a word, entered by the user, from the JSON file
#need to account for someone inputting something that is not a word or is not in the dictionary = if/else statements in the function
#needs to account for case sensitivity = .lower()
#need to use SequenceMatcher and get_close_matches from 'difflib' library to get words close enough to the words entered by the user
#can use "\u0332".join() to underline text written in the brackets
#Need to account for people deciding if the word they are corrected with is the word they are looking for
#clean up the way definition is presented by creating loop that loops through the items in the key and prints them individually
#clean up entire code putting all previous steps into the function so it only activates when called (e.g. importing json and difflib in the function)

def translate():
    import json
    import difflib
    from difflib import SequenceMatcher
    from difflib import get_close_matches
    data=json.load(open("data.json"))
    w=input("Enter Word: ").lower()
    k=0
    if w in data:
        print("Definition/s:")
        for i in data[w]:
            k+=1
            print(str(k)+". " + i)
        return
    elif w.capitalize() in data:
        print("Definition/s:")
        for i in data[w.capitalize()]:
            k+=1
            print(str(k)+". " + i)
        return
    elif w.upper() in data:
        print("Definition/s:")
        for i in data[w.upper()]:
            k+=1
            print(str(k)+". " + i)
        return
    elif len(get_close_matches(w,data.keys(),cutoff=0.6))>0:
        yn=(input("Did you mean %s instead? \nEnter Y or N: " % get_close_matches(w,data.keys())[0]))
        if yn == "Y":
            print("Definition/s:")
            for i in data[get_close_matches(w,data.keys())[0]]:
                k+=1
                print(str(k)+". " + i)
            return
        elif yn == "N":
            print("Then this word does not exist in this dictionary")
            return
        else:
            print("Didn't enter Y or N, program will end and the word entered was not in this dictionary")
            return
    else:
        print("This word does not exist in this dictionary")
        return
translate()
