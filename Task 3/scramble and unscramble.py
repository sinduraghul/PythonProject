import random

words = ["python", "javascript", "java", "automation", "pytest", "guvi", "selenium"]
word=random.choice(words)
scrambled = "".join(random.sample(word, len(word)))

print("Unscramble this word:",scrambled)
attempts = 3
while attempts > 0:
    guess = input("your guess: ").lower()
    if guess == word.lower():
        print("Correct! You guessed the unscrambled word!")
        break
    else:
        attempts -= 1
        if attempts > 0:
           print("you guessed it wrong:", attempts)
        else:
            print("😢 Out of attempts!:")