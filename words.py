words=["hey","there","it's","me","mario","egads!","did","you","see","my","new","movie","Enough"]

letters={"h","t"}

# function for question 1

def upper_words(word_list):
    """input a list of words as strings. function will print in uppercase"""
    for word in word_list:
        print (word.upper()) 

# changes for question 2

def e_only_upper_words(word_list):
    """input a list of words as strings. Function will print if the word begins with an e"""
    for word in word_list:
        if word.startswith("e") or word.startswith("E"):
            print(word)

# changes for question 3

def specific_words(word_list,letter_set):
    """input a list of words as strings and a set of letter strings.function will print if the word begins with any letter in the set"""
    for word in word_list:
        for letter in letter_set:
            if word.startswith(letter):
                print (word.upper())
                break

# tests

upper_words(words) 
# should be HEY, THERE, IT'S, ME, MARIO etc....

e_only_upper_words(words)
#should be 'egads!'

specific_words(words,letters)






