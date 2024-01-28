# This code will take a string and make the characters alternate
# between upper and lower case

string = "Have a lovely day!" # This variable holds the original string
print(f"Original string: {string}")
alternating = "" # This variable holds the new alternating string

# This for loop edits each even numbered iteration to an uppercase
# letter, and each odd numbered iteration to a lowercase letter.
for index, letter in enumerate(string):
    if index % 2 == 0:
        alternating += letter.upper()
    else:
        alternating += letter.lower()

print(f"Alternating letters: {alternating}")

# The next section of code will take a string and make each word 
# alternate between upper and lower case.

# This variable splits the string into single words in a list
words = string.split()
# This variable will hold the new alternating sentence
new_sentence = []

# This for loop edits each even numbered iteration from the list of
# words into all capital letters, and each other word into all
# lowercase letters, and adds it to the new sentence
for index, word in enumerate(words):
    if index % 2 == 0:
        new_sentence.append(word.upper())
    else:
        new_sentence.append(word.lower())

# This will join the alternately capitalised words into a sentence
# inclduing spaces and print.
print("Alternating words: " + " ".join(new_sentence))
