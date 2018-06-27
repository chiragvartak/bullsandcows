import sys
from utils import cows, bulls
from words import WORDS
import random

MAX_GUESSES = 5

original = random.choice(WORDS)

print("Let's start the game.")
print("")

guessNumber = 1
while guessNumber <= MAX_GUESSES:
    guess = input("Guess number " + str(guessNumber) + ": ")
    print("Cows:", cows(original, guess), "Bulls:", bulls(original,guess))
    guessNumber += 1
    print("")

    if original.lower() == guess.lower():
        print("Yay, you win, you guessed it right! Congrats!")
        sys.exit(0)

print("Sorry, you could not guess the word, you lost.")
print("The word was: " + original)