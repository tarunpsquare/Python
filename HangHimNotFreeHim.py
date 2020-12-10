# -*- coding: utf-8 -*-
"""
@author: Tarun Purohit tarunpp2001@gmail.com
"""
#Python Project:HANG HIM NOT FREE HIM
#Implemented a game in python which is very similar to Hangman.
#Turtle library used to draw the stick figure of the man.
import random, time, turtle,sys
def movies():
    movies=["DJANGO UNCHAINED", "AVATAR", "INCEPTION", "DUNKIRK", "THE REVENANT"]
    chosenword=random.choice(movies)
    chosenwordlist=list(chosenword)
    attempts = (len(chosenword) + 3)
    print("Your movie has been selected at random. Let the guessing game begin!\n")
    print("A hint to make things easier:")
    if chosenword=='AVATAR':
        print("Graphical representation of a user or the user's character or persona.\n")
    elif chosenword=='DJANGO UNCHAINED':
        print("DJ Not chained.\n")
    elif chosenword=='INCEPTION':
        print("Entering dreams.\n")
    elif chosenword=='DUNKIRK':
        print("World War 2, Allied forces, German army.\n")
    elif chosenword=='THE REVENANT':
        print("Fur trading expedition, 1820s, bear, abandnded by hunting team.\n")
    elif chosenword=='THE EXORCIST':
        print("When a 12-year-old girl is possessed by a mysterious entity, her mother seeks the help of two priests to save her.\n")
    elif chosenword=='JURASSIC PARK':
        print("A pragmatic palaeontologist visiting an almost complete theme park is tasked with protecting a couple of kids after a power failure causes the park's cloned dinosaurs to run loose.\n")
    elif chosenword=='BACK TO THE FUTURE':
        print("A 17-year-old high school student, is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend, an eccentric scientist.\n")
    elif chosenword=='THE DARK KNIGHT':
        print("When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, a masked vigilante must accept one of the greatest psychological and physical tests of his ability to fight injustice.\n")
    elif chosenword=='GLADIATOR':
        print("A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.\n")
    print("The number of allowed guesses for this word is:", attempts)
    guesses(chosenword, chosenwordlist, attempts)
    
    
def places():
    
    places=["QUEBEC", "ILLINOIS", "NEW YORK", "MELBOURNE", "SICILY"]
    chosenword=random.choice(places)
    chosenwordlist=list(chosenword)
    attempts = (len(chosenword) + 3)
    print("Your places has been selected at random. Let the guessing game begin!\n")
    print("A hint to make things easier:")
    if chosenword=='QUEBEC':
        print("Eastern province of Canada and the oldest city of Canada. Home to attractions such as Basilica of Sainte-Anne-de-Beaupré and  Place Royale. Also constitutes of the French speaking population of Canada.\n")
    elif chosenword=='ILLINOIS':
        print("It is a midwestern state bordering Indiana in the east and the Mississippi River in the west. Nicknamed the Prairie State, it's marked by farmland, forests, rolling hills and wetlands. Chicago, one of the largest cities in the U.S, is in the northeast on the shores of Lake Michigan. \n")
    elif chosenword=='NEW YORK':
        print("Home to the Empire state building and also the most busiest place in U.S.A.\n")
    elif chosenword=='MELBOURNE':
        print("Coastal capital of the southeastern Australian state of Victoria. At the city's centre is the modern Federation Square development, with plazas, bars, and restaurants by the Yarra River.Also one of the most sought after places in Australia after Sydney.\n")
    elif chosenword=='SICILY':
        print("One of the most beautiful and historic places in Italy. The largest Mediterranean island, is just off the toe of Italy's boot. Its rich history is reflected in sites like the Valley of the Temples, the well-preserved ruins of 7 monumental, Doric-style Greek temples, and in the Byzantine mosaics at the Cappella Palatina, a former royal chapel in capital city Palermo.\n")
    print("The number of allowed guesses for this word is:", attempts)
    guesses(chosenword, chosenwordlist, attempts)   

    
def animals():
    
    animals=["MONKEY", "CHEETAH", "BLACK MAMBA", "CROCODILE"]
    chosenword=random.choice(animals)
    chosenwordlist=list(chosenword)
    attempts = (len(chosenword) + 3)
    print("Your animal has been selected at random. Let the guessing game begin!\n")
    print("A hint to make things easier:")
    if chosenword=='MONKEY':
        print("Their fur is generally a shade of brown or black, and their muzzles, like those of baboons, are doglike but rounded in profile, with nostrils on the upper surface.\n")
    elif chosenword=='CHEETAH':
        print("Large cat native to Africa and central Iran. It is the fastest land animal, capable of running at 80 to 128 km/h, and as such has several adaptations for speed, including a light build, long thin legs and a long tail.\n")
    elif chosenword=='BLACK MAMBA':
        print("Species of highly venomous snake belonging to the family Elapidae. It is native to parts of sub-Saharan Africa.\n")
    elif chosenword=='CROCODILE':
        print("Large semiaquatic reptiles that live throughout the tropics in Africa, Asia, the Americas and Australia.have powerful jaws with many conical teeth and short legs with clawed webbed toes.\n")
    print("The number of allowed guesses for this word is:", attempts)
    guesses(chosenword, chosenwordlist, attempts)


def guessedletter(guesslist):
    print("Your Secret word is: " + ''.join(guesslist))
    
    
def guesses(chosenword, chosenwordlist, attempts):
    guess=''
    hang=0
    guesslist=list(guess)
    len(guess)==len(chosenword)
    rope=turtle.Turtle()
    rope.penup()
    rope.goto(-40.00,100.00)
    rope.back(100)
    rope.right(90.00)
    rope.pendown()
    rope.forward(300)
    rope.penup()
    rope.back(300)
    rope.pendown()
    rope.left(90)
    rope.forward(140)
    rope.right(90)
    rope.forward(40)
    for n in chosenwordlist:
        guesslist.append(' _ ')
    guessedletter(guesslist)
    while True:
         letter=input("Enter a letter\n")
         letter=letter.upper()
         if letter in guesslist:
             print("This letter has already been guessed.\n")
             print("Guess a different letter.\n")
         else:
             attempts=attempts-1
             if letter in chosenwordlist:
                 print("Bang on!")
                 if attempts>0:
                     print("You have: ", attempts," :attempts left.")
                 for i in range(len(chosenwordlist)):
                     if letter == chosenwordlist[i]:
                         letterindex = i
                         guesslist[letterindex] = letter
                 guessedletter(guesslist)
                
             else:
                 print("Oops! Try again.")
                 hang=hang+1
                 hangman(hang, chosenword)
                 if attempts > 0:
                     print("You have ", attempts, 'guess left!')
                 guessedletter(guesslist)
         joinedList = ''.join(guesslist)
         if joinedList.upper() == chosenword.upper():
             print("Yay! you won.\nHang Him Not, Free Him")
             print("Do you wish to play again?\n")
             replay=input("Y for yes and anything else to quit")
             replay=replay.upper()
             if replay=='Y':
                 user()
             else:
                 print("Thank you for playing Hang Him Not Free Him! Hope you had fun.\n")
                 sys.exit()
         elif attempts == 0:
             print("Too many Guesses!, Sorry better luck next time.")
             print("Hang Him, Not Free Him.\n")
             print("Do you wish to play again?\n")
             print("The secret word was: "+ chosenword())
             
             replay=input("Y for yes and anything else to quit")
             replay=replay.upper()
             if replay=='Y':
                 turtle.clearscreen()
                 user()
             else:
                 print("Thank you for playing Hang Him Not Free Him! Hope you had fun.\n")
                 time.sleep(2)
                 sys.exit()
             


def hangman(hang, chosenword):
    if hang==1:
        turtle.penup()
        turtle.goto(0.00,0.00)
        turtle.setheading(0.00)
        turtle.pendown()
        turtle.circle(30)
    elif hang==2:
        turtle.right(90)
        turtle.forward(30)
        turtle.right(30.00)
        turtle.forward(40)
        turtle.penup()
    elif hang==3:
        turtle.back(40)
        turtle.left(60.00)
        turtle.pendown()
        turtle.forward(40)
        turtle.penup()
    elif hang==4:
        turtle.back(40)
        turtle.right(30.00)
        turtle.pendown()
        turtle.forward(60)
        turtle.right(30.00)
        turtle.forward(40)
        turtle.penup()
    elif hang==5:
        turtle.back(40)
        turtle.left(60.00)
        turtle.pendown()
        turtle.forward(40)
        print("Hang Him, Not Free Him\n")
        print("The secret word was: "+ chosenword)
        print("Do you wish to play again?\n")
        replay=input("Y for yes and anything else to quit")
        replay=replay.upper()
        if replay=='Y':
            turtle.clearscreen()
            user()
        else:
            print("Thank you for playing Hang Him Not Free Him! Hope you had fun.\n")
            sys.exit()
            
        

def user():
    turtle.clearscreen()
    name=input("Hey there! Enter your name:\n")
    if name.isalpha() == True:
        print("Hello", name.capitalize(), "let's start playing Hang Him Not Free Him!")
        time.sleep(1)
        print("The objective of the game is to guess the secret word chosen by the computer.")
        time.sleep(1)
        print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
        time.sleep(2)
        print("Let the fun begin!")
        time.sleep(1)
        choice=int(input("What are you most confident about?\n 1.Movies\n 2.Places\n 3.Animals\n"))
        if choice==1:
            movies()

        elif choice==2:
            places()

        elif choice==3:
            animals()
        else:
            print("Wrong entry. Restart.")
            user()
    else:
        print("Invalid. Retype name.")
        user()
user()



