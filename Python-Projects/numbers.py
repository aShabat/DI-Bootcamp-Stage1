from random import randint

secret = randint(1, 100)
for _ in range(7):
    guess = int(input("Guess a number: "))
    if guess == secret:
        print("Bingo!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too hight")
