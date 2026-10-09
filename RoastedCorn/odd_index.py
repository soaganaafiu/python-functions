def odd_index(word):


    for number in range(len(word)):

        if number % 2 != 0:

    return word[number]


word_used = "semicolon"
print(odd_index(word_used))
