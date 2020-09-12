from random import randint

rps = ["rock", "paper", "scissors"]

r = "rock"
p = "paper"
s = "scissors"

rock = "r"
paper = "p"
scissors = "s"

w = "win"
l = "lose"

player = ""
computer = rps[randint(0, 2)]

game = 0

while game < 1:
    game += 1
    player = input("Rock, Paper, or Scissors?: ")
    if player == computer:
        print("Tie")
    else:
        if player == r or player == rock:
            if computer == p or player == paper:
                print(l)
            else:
                print(w)
        elif player == p or player == paper:
            if computer == r or player == rock:
                print(w)
            else:
                print(l)
        elif player == s or player == scissors:
            if computer == r or player == rock:
                print(l)
            else:
                print(w)
        elif player_choice == computer:
            print("Found it")
        else:
            print("Wrong input.")
            game -= 1


#
player_choice = ""
if player == rock or player == r:
    player_choice = "rock"
elif player == paper or player == p:
    player_choice = "paper"
elif player == scissors or player == s:
    player_choice = "scissors"
else:
    print("Fix code")

print("\nComputer choose: " + computer + "\n" +"Player choose: " + player_choice)