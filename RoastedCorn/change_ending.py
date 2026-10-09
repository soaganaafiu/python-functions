def word_length(word):

    length = len(word)

    return length



def word_adding(word):

    if word_length(word) < 3:

        return word

    elif word[-3] == "i" and word[-2] == "n" and word[-1] == "g":

        return word + "ly"


    elif word_length(word) > 3:

        return word + "ing"



word_enter = input("Enter a word: ")

print(word_adding(word_enter))
