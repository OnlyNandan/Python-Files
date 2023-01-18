import random
import time
print("\n_________________Hangman Game_________________\n")
words = "ape cat dog baboon elephant giraffe apple coconut monkey rubik mice mouse pineapple android apple house fence python terran fire policeman zebra lion luffy".split()
word=random.choice(words)
print("\n Guess the characters of the random word")
HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
        |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
    |   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
   ========''','''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
   ========''']

guesses=""
chance=7
while chance>0:
    w=0
    for char in word:
        if char in guesses:
            time.sleep(0.5)
            print(char,end=" ")
        else:
            time.sleep(0.1)
            print("_",end=" ")
            w+=1
    print(HANGMANPICS[chance-1])
    if w==0:
        time.sleep(2)
        print("\n\nCongratulations! You beat the game!!!! \n")
        print("The Word is: ",word,"\n\n")
        print(HANGMANPICS[chance-1])
        break
    print()
    guess=input("Guess A character of the word: ")
    guesses += guess
    if guess not in word:
        chance -=1
        print(HANGMANPICS[chance])
        print("Wrong Character!!!")
        print("You Have",chance,"more chances to guess the correct word")
        if chance ==0:
            print("Better Luck Next Time")
            print("The Word is: ",word,"\n\n")
