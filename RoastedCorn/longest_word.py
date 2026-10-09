def longest_word(words):

    longest = ""

    for word in words:

        length = len(word)

        if word > longest:

            longest = word

    return len(longest)
    



list_of_words = ["great", "smart", "yamarita", "ketchup", "bottle"]

print(longest_word(list_of_words))
