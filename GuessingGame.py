import random

number = random.randrange(10)
guesses_left = 5

print("Guess The Number!")
state = "none" 
while guesses_left > 0:
        guess = int(input("Guess A Number : "))
        guesses_left -= 1

        if(guess < number):
            print("Guess a Number Higher Than ", guess)

        if(guess > number):
            print("Guess a Number Lower Than ", guess)

        if(guess == number):
            print("You Won!")
            state = "win"
            guesses_left = 0

        if (guesses_left <= 0 and state != "win"):
            print("You Lose!")
