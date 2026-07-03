import random

print("Let's play hangman!")
wordlist = [apple, horse, banana, blanket, table, piano, globe]
picked_word = random.choice(wordlist)
length = len(picked_word)
display = "_ " * length
print(display)
lives = 6
