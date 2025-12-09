import random

num= random.randint(1,20)
guess=int(input("Enter a number: "))
while num != guess: #keeps running as long as the guess is not equal to the secret number
    if guess < num:
        print("Too low")
        guess=int(input("Enter a number again: "))
    elif guess > num:
        print("Too high")
        guess=int(input("Enter a number again: "))
    else:
        break
print("You guessed it right!!")