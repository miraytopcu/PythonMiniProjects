import random
tv_series = ["adını feriha koydum", "good luck charlie", "ufak tefek cinayetler", "better call saul", "gilmore girls"]
movies = ["hababam sınıfı tatilde", "the sixth sense", "five feet apart", "organize işler sazan sarmalı", "ay lav yu"]
celebrities = ["bülent ersoy", "seda sayan"]
songs = ["ben şarkımı söylerken", "set fire to the rain"]
items = tv_series + movies + celebrities + songs

selected_item = random.choice(items)

def categories(selected_item):
    if selected_item in tv_series:
        print("The category is TV Series!")
    if selected_item in movies:
        print("The category is movies!")
    if selected_item in celebrities:
        print("The category is celebrities!")
    if selected_item in songs:
        print("The category is songs!")

def path(selected_item):
    word = selected_item
    output = ""
    for letter in word:
        if letter.isalpha() == True:
            output += "_ "
        if letter == " ":
            output += " "
    print(output)

def hangman():
    print("Welcome to Hangman!")
    print("Try to guess the word. You can only make 6 wrong guesses.")
    
    word = selected_item
    guessed_letters = []
    wrong_guesses = 0
    
    while wrong_guesses < 6:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            if set(word) == set(guessed_letters):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            wrong_guesses += 1
            print("Wrong guess! You have", 6 - wrong_guesses, "guesses left.")
    if wrong_guesses == 6:
        print("\nSorry, you ran out of guesses. The word was:", word)

categories(selected_item)
path(selected_item)