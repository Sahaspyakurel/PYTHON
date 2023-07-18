# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Check if the sentence starts with 'y' or 'p'
if sentence.startswith('y') or sentence.startswith('p'):
    print("The sentence starts with 'y' or 'p'.")
else:
    print("The sentence does not start with 'y' or 'p'.")
