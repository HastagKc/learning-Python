# 4. Program to check if a character is a vowel or consonant.
# vowels a e i o u 

# def check_vowel_consonant(letter):
#     if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'):
#         print("Vowel")
#     else:
#         print("consonant")

# letter = input("Enter any letter: ")
# check_vowel_consonant(letter.lower())


def check_vowel_consonant_with_list(char):
    vowels_list = ['a','e','i','o','u']
    char = char.lower()
    if char in vowels_list:
        print("Vowel")
    else:
        print("Consonant")

char = input("Enter any character: ")
check_vowel_consonant_with_list(char)  

