import random
import time
import string
import pyperclip
from playsound import playsound
bao=0
percent = 0
lj=0
sing=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
time.sleep(1)
print("\t\t\tWelcome to Pydex Online gaming Center\n\n")
print("This python program has been made by IIT Aspirants and Jay")
time.sleep(1)
while(bao==0):
    
    time.sleep(1)
    print(" -----------------------")
    time.sleep(0.3)
    print(" |>0>Random Game       |")
    time.sleep(0.3)
    print(" |>1>Guess The Number  |")
    time.sleep(0.3)
    print(" |>2>Dice Throw        |")
    time.sleep(0.3)
    print(" |>3>Random Password   |")
    time.sleep(0.3)
    print(" |>4>Hangman           |")
    time.sleep(0.3)
    print(" |>5>RockPaper         |")
    time.sleep(0.3)
    print(" |>6>HIgh Card         |")
    time.sleep(0.3)
    print(" |>7>Guess The Song    |")
    time.sleep(0.3)
    print(" |>8>Credits           |")
    time.sleep(0.3)
    print(" |>9>Exit              |")
    time.sleep(0.3)
    print(" -----------------------")

    j=input("Enter the Name/Number of the game you want to play:- ")
    if(j=="0" or j=="guess the number" or j=="guess"):
        j=random.randint(1,5)
        j=str(j)
        print(j)
    if(j=="1" or j=="guess the number" or j=="guess"):
        time.sleep(2)
        number = random.randint(1, 100)
        attempts = 0
        guess = 0
        while guess != number:
            guess = int(input('Guess a number between 1 and 100: '))
            attempts += 1
            if guess == number:
                print('Correct! You used', attempts, 'attempts!')
                break
            elif guess < number:
                print('Go higher!')
            else:
                print('Go lower!')
    elif(j=="2" or j=="dice throw" or j=="dice"):
        dice=['''
        -----
        |   |
        | o |
        |   |
        -----''','''

        -----
        |o  |
        |   |
        |  o|
        -----''','''

        -----
        |o  |
        | o |
        |  o|
        -----''','''

        -----
        |o o|
        |   |
        |o o|
        -----''','''

        -----
        |o o|
        | o |
        |o o|
        -----''','''

        -----
        |o o|
        |o o|
        |o o|
        -----''']
        d=random.randint(1,6)
        print(dice[d-1])
        print(d)
    elif(j=="3" or j=="random password" or j=="password"):
        length = int(input("Enter length of the password: "))
        characterList = ""
        characterList += string.digits
        characterList += string.ascii_letters
        characterList += "@" 
        password = []
 
        for i in range(length):
            randomchar = random.choice(characterList)
            password += randomchar
 
        pwd="".join(password)
        print("The random password is " + pwd ,end="\n\n")
        pyperclip.copy(pwd)
        time.sleep(2)
        print(">>The Random Password has been copied to your clipboard.")
    elif(j=="4" or j=="hangman" or j=="hang"):
        print("\n_________________Hangman Game_________________\n")
        apc=input("Would you like to play Country or Word Hangman??? (c/w): ")
        if(apc=="c"):
            words=['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
        else:
            words = "ape cat dog baboon elephant giraffe apple coconut monkey rubik mice mouse pineapple android apple house fence python terran fire policeman zebra lion luffy".split()
        word=random.choice(words)
        capword=word
        word=word.lower()
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
                print("The Word is: ",capword,"\n\n")
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
                    print("The Word is: ",capword,"\n\n")
    elif(j=="5" or j=="rock" or j=="paper"):


        rock_ascii = '''
           _______
        ---'   ____)
             (_____)
             (_____)
             (____)
        ---.__(___)
        '''

        paper_ascii = '''
           _______
        ---'   ____)____
                 ______)
                 _______)
                _______)
        ---.__________)
        '''

        scissors_ascii = '''
           _______
        ---'   ____)____
                 ______)
              __________)
             (____)
        ---.__(___)
        '''

        print("Welcome to the Rock Paper Scissors game!!!")
        game_img_ascii = [rock_ascii, paper_ascii, scissors_ascii]

        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

        if user_choice >= 3 or user_choice < 0:
         print("You typed an invalid number you lose!")
        else:
         print(game_img_ascii[user_choice])
         com_choice = random.randint(0, 2)

         print("Computer Choose: ")
         print(game_img_ascii[com_choice])


        if user_choice == 0 and com_choice == 2:
           print("You win!")
        elif com_choice == 0 and user_choice == 2:
           print("You lose!")
        elif com_choice > user_choice:
           print("You lose!")
        elif user_choice > com_choice:
           print("You win!")
        elif com_choice == user_choice:
           print("Its a draw!")
    elif(j=="8" or j=="credit" or j=="credit"):
        time.sleep(1)
        print("Driver:- Nandan,Guneev")
        print("Navigator:- Ahmed and Jay")
        print()
        print("Game Credits", end ="\n\n")
        print("Guess the Song, HangMan, Dice Throw, Guess the Number and Random Password -Nandan")
        print()
        print("Rockpaper - Ahmed")
        print()
        print("High Card - Guneev ")
        
    elif(j=="9" or j=="exit"):
        break
    elif(j=="6" or j=="highcard" or j=="high"):
        suits = ["clubs", "diamonds", "hearts", "spades"]
        faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "jack", "queen", "king", "ace"]
        keep_going = True
        while keep_going:
         my_face = random.choice(faces)
         my_suit = random.choice(suits)
         your_face = random.choice(faces)
         your_suit = random.choice(suits)
         print("I have the", my_face, "of", my_suit)
         print("You have the", your_face, "of", your_suit)
         if faces.index(my_face) > faces.index(your_face):
             print("I win!")
         elif faces.index(my_face) < faces.index(your_face):
             print("You win!")
         else:
             print("It's a tie!")
         answer = input("Hit [Enter] to keep going, any key to exit: ")
         keep_going = (answer == "")
    elif(j=="7" or j=="guess the song" or j=="song"):
        score=0
        var=1
        
        while(var<=5):
            
            randsong=random.choice(sing)
            
            if(randsong==1):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("1.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="why this kolaveri di"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was Why This Kolaveri Di")                    
            elif(randsong==2):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("2.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="never gonna give you up"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was Never Gonna Give You Up")

            elif(randsong==3):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("3.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="o sanam"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was O Sanam")
            elif(randsong==4):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("4.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="wavin flag"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was Wavin' Flag")
            elif(randsong==5):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("5.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="gangnam style"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was Gangnam Style")
            elif(randsong==6):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("6.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="jimikki kammal"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was Jimikki Kammal")
            elif(randsong==7):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("7.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="bohemian rhapsody"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was Bohemian Rhapsod")
            elif(randsong==8):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("8.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="i was never there"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was I was Never There")
            elif(randsong==9):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("9.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="take me home country roads"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was Take Me Home, Country Roads")
            elif(randsong==11):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("11.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="moves like jagger"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was Moves like Jagger")
            elif(randsong==10):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("10.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="i aint worried"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was i aint worried")



            elif(randsong==14):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("14.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="gangsta paradise"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was Gangsta paradise")
            elif(randsong==15):
                print("Time For Song Number ",var)
                time.sleep(1)
                playsound("15.mp3")
                gsong=""
                gsong=input("Enter the name of the song:- ")
                gsong=gsong.lower()
                if(gsong=="despacito"):
                    time.sleep(1)
                    print("Correct Guess Well done")
                    score=score+1
                    print("You have Won 1 point")
                else:
                    print("Wrong Guess")
                    print("The song was Despacito")
            
            else:
                continue
            sing.remove(randsong)
            var=var+1
    if(j=="7" or j=="guess the song" or j=="song"):
         print("your score for guess the song is",score)
  
    ansl=input("Would You like to replay the pydex program?(y/n)")
    ansl=ansl.lower()
    if(ansl=="y" or ansl=="yes"):
      continue
    else:
      print("Thank you for playing our games. Hope you had fun")
      break
    
