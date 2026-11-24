import random

words = ["apple", "tiger", "chair", " mango", "river"]

word = random.choice(words).strip()
guessed = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if all(letter in guessed for letter in word):
        print("Congratulations! You Won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter!")
        continue

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Remaining attempts:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("Correct Word:", word)