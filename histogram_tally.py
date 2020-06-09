# from DC immersive learning portal
# Write a letter_histogram program that asks the user for input, and prints a dictionary
# containing the tally of how many times each letter in the alphabet was used in the word.

# Given a histogram tally (one returned from either letter_histogram
# or word_histogram), print the top 3 words or letters.

word = input("Give me a word: \n")
letter_list = {}
for letter in word:
    if (letter in letter_list):
        letter_list[letter] += 1
    else:
        letter_list[letter] = 1

print(letter_list)

top_3 = []
for letter in letter_list:
    if letter_list[letter] > highest:
        highest = letter_list[letter]

print(highest)
