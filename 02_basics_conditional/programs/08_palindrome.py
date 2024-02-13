# a word, phrase, or sequence that reads the same backwards 
# as forwards, e.g. madam or nurses run


def reversed_word(word):
    # creating new variable because string is immutable 
    rev_word = ""
    for i in word:
        rev_word = i + rev_word
    return rev_word


word = "madam"

if word == reversed_word(word):
    print("palindrome")
else:
    print("Not a Palindrome")