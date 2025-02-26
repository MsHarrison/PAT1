from random import randint

""" Guessing Game - Ardle 
    A CLI-based word guess game
    Ms Harrison
    February 2025 """

print("ARDLE WORD GUESS GAME")
print("---------------------")
print()

gameplay = True

def instructions():
    print("Put gameplay instructions here...")

def playgame():
    wordlist = open("words.txt", "r")
    words = []
    for each in wordlist:
        words.append(each)
    randword = randint(1,100)
    print(words[randword])
    wordguess = []
    numGuesses = 0
    keepPlaying = True
    while keepPlaying:
        letterGuess = input("Enter a letter: ")
        position = 0
        for each in randword:
            if letterGuess == each:
                wordguess[position] = letterGuess
            position += 1
        numGuesses += 1
        if numGuesses == 6:
            print("That was your last guess")
            keepPlaying = False
            print("Results are in!")
            print("---------------")
            print(wordguess)
        elif wordguess == randword.split():
            print("Yay! You guessed the word!")
            print("Results are in!")
            print("---------------")
            print(wordguess)
        
        



while gameplay:
    print("Menu options")
    print("------------")
    print("Would you like to see the (i)nstructions, start a (n)ew game or (q)uit?")

    selection = input()
    if selection.lower() == "i":
        instructions()
    elif selection.lower() == "n":
        playgame()
    elif selection.lower() == "q":
        print("Thanks for playing!")
        gameplay = False
    else:
        print("That's not a valid option.")





