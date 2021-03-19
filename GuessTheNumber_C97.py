import random

print("Number Guessing Game!")

print("Guess a number between 1 and 9 ")

num = random.randint(1,9) 
chances = 0
while chances < 3:
    choice = int(input("Enter your guess : "))
    if(choice == num):
        print("Yay! you won!")
        break 
    elif(choice < num):
        print("Too Low!")
        chances += 1
    else:
        print("Too High!")
        chances += 1
    
if not chances <3:
    print("You lose! The number is "+str(num))
    
