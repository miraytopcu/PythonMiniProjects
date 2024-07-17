# You must guess a secret three-digit number based on clues.
# Pico: your guess has a correct digit, in the wrong place.
# Fermi: your guess has a correct digit in the correct place.
# Bagels: your guess has no correct digits.
# You have 10 tries to guess the secret number.

import random

def getSecretNum():
    secret_number = str(random.randint(100,999))
    return secret_number

def getClues(guess, secret_number):
    # pico: 1 correct digit, wrong place
    # fermi: 1 correct digit, correct place
    # bagels: no correct

    if guess == secret_number:
        return "Congratulations! You win"
    
    clues = []
    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            clues.append("fermi")
        elif guess[i] in secret_number:
            clues.append("pico")
    if len(clues) == 0:
        return "bagels"
    else: 
        clues.sort()
        return " ".join(clues)
    

secretNum = getSecretNum()
chances = 10
print("I have a secret number. Let's try to guess! \nYou have 10 tries to guess. Good Luck!")
numGuesses = 1

while numGuesses <= chances:
    guess = ""
    find = True
    # while len(guess) != len(secretNum) or not guess.isdecimal():
    while find:
        guess = input(f"Your {numGuesses}.guess: ")
        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1

        if guess == secretNum:
            find = False
        if numGuesses > chances:
            print(f"You Lost!! \nThe answer is{secretNum}")
            find = False

print("Thanks for playing!")


