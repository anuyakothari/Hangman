import random

print("Let's play hangman!")
wordlist = [apple, horse, banana, blanket, table, piano, globe]
picked_word = random.choice(wordlist)
length = len(picked_word)
display = "_ " * length
print(display)
lives = 6

wordlist = ["grape", "horse", "chair", "blanket", "table", "piano", "globe", "shoe", "pencil", "paint", "ruler", "quail", "history", "beach", "dolphin", "rope", "flower", "month", "birthday", "light", "flag", "state", "insect", "story", "globe", "signature", "child" ]

guesses = []


def play_again():
    again = input("Play again? (yes/no): ").lower()

    while again != "yes" and again != "no":
        again = input("Invalid input. Play again? (yes/no): ").lower()

    if again == "no":
        quit()
    if again == "yes":
        guesses.clear()
        run_hangman()


def run_hangman():
    while True:
        picked_word = random.choice(wordlist)
        length = len(picked_word)
        display = "_ " * length
        print(display)
        lives = 6

        while lives > 0:
            print("Lives left:" + str(lives))

            letter = input("Guess a letter: ")
            letter = letter.lower()

            if letter in guesses:
                print("Already guessed!")
                if letter not in picked_word:
                    lives += 1

            if letter.isalpha():
                guesses.append(letter)

                if len(letter) > 1:
                    print("Not a valid guess. Please enter a single letter.")

                elif letter in picked_word:
                    index = picked_word.index(letter)
                    display = display[:index * 2] + letter + display[index * 2 + 1:]

                    print(display)

                    if "_" not in display:
                        print("Congratulations! You've guessed the word:", picked_word)
                        play_again()

                else:
                    lives -= 1
                    print("Letter not found.")
                    print(display)

            else:
                print("Please enter a valid letter.")

        print("Out of lives, game over!")
        print("The word was", picked_word)
        play_again()


run_hangman()
