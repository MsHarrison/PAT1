""" Guessing Game - Ardle 
    A CLI-based word guessing game
    Ms Harrison
    February 2025 """
from random import randint

print("ARDLE WORD GUESS GAME")
print("---------------------")
print()

gameplay = True

def instructions():
    print("Put gameplay instructions here...")


while gameplay:
    print("Menu options")
    print("------------")
    print("Would you like to see the (i)nstructions, start a (n)ew game or (q)uit?")

    selection = input()
    if selection.lower() == "i":
        instructions()
    elif selection.lower() == "n":
        wordlist = open("words.txt", "r")
        words = []
        for each in wordlist:
            words.append(each)
        randnum = randint(0,len(words) - 1)
        randomword = words[randnum]
        print(randomword)
        wordguess = ["_", "_", "_","_","_"]
        randWordAsList = list(randomword.strip())
        numGuesses = 0
        keepPlaying = True
        while keepPlaying:
            print(wordguess)
            print()
            letterGuess = input("Enter a letter: ")
            position = 0
            for each in randWordAsList:
                if letterGuess == each:
                    wordguess[position] = letterGuess
                position += 1
            numGuesses += 1
            if numGuesses == 10 and wordguess != randWordAsList:
                print("That was your last guess")
                print(f'The secret word was {randomword}!')
                print("Better luck next time!")
                keepPlaying = False
            elif wordguess == randWordAsList:
                print("Yay! You guessed the word!")
                keepPlaying = False
    elif selection.lower() == "q":
        print("Thanks for playing!")
        gameplay = False
    else:
        print("That's not a valid option.")