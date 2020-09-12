from random import randint

r1 = randint(0, 5)
guess = ""
tries = 1


while guess != r1:
    guess = int(input("Enter your guess: "))
    tries += 1
    if tries > 3:
        print("You lose")
        guess = r1
    else:
        if guess == r1:
            print("Win")
        elif guess < r1:
            print("Too small")
        else:
            print("Too big")

