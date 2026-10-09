
def word_length(word):

    length = len(word)

    return length



def picker(text):

    size = word_length(text)

    if (size < 2):

        return ""

    return text[0],text[1],text[-2],text[-1]



word_enter = input("Enter a word: ")

word_picker = picker(word_enter)

print(word_picker)
