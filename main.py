import random

n = random.randint(1, 100)
a = -1
guesses = 0

print("Welcome to a Simple Guess Game!")

while (a != n):

    a = int(input("Guess the number: "))
    if a < n:
        print("Higher Number Please!")
    elif a > n:
        print("Lower Number Please!")
    guesses += 1

print(f"You guessed the number {n} in {guesses} guesses!")


                

   
