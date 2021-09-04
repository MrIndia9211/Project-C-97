import random

print("NUMBER GUESSING GAME")

number = random.randint(1,9)

chances = 0

print("GUESS ANY NUMBER BETWEEN 1 To 9")


while chances<5:
    guess = int(input("ENTER YOUR GUESS"))

    if guess == number:
  
        print("You Win! Congratulations!")

        break
    
    elif guess < number:
        print("Your Guess is too Low")
        print("Guess a Number higher than this")

    else:
        print("Your Guess is too high")
        print("Guess a Number lesser than this")
    
   

if chances==5 and guess!= number:
    print("YOU LOSE")
    