'''
Create a game that will challenge you against the computer in a game of rock paper scissors. 
The user will input whether they choose rock paper or scissors and the computer will also choose one. 
The first to two will win the game
'''
#import choice
from random import choice

#round count
round = 1

#win count
computer = 0
player = 0

#choice storage
player_rps = ""
computer_rps = ""

#game runner
while computer != 2 and player != 2:
    #choice generator
    computer_rps = choice(["rock", "paper", "scissors"])    
    player_rps = input("rock, paper, scissors")

    #round win determiner
    if player_rps in computer_rps:
        print(f"player: {player_rps}")
        print(f"computer: {computer_rps}")
        print("round {} tie".format(round))
        print("{1} : {0}".format(computer, player))
    elif player_rps == "rock" and computer_rps == "paper":
        print(f"player: {player_rps}")
        print(f"computer: {computer_rps}")
        print("round {} computer wins".format(round))
        computer += 1
        print("{1} : {0}".format(computer, player))
    elif player_rps == "rock" and computer_rps == "scissors":
        print(f"player: {player_rps}")
        print(f"computer: {computer_rps}")
        print("round {} player wins".format(round))
        player += 1
        print("{1} : {0}".format(computer, player))
    elif player_rps == "paper" and computer_rps == "scissors":
        print(f"player: {player_rps}")
        print(f"computer: {computer_rps}")
        print("round {} computer wins".format(round))
        computer += 1
        print("{1} : {0}".format(computer, player))
    elif player_rps == "paper" and computer_rps == "rock":
        print(f"player: {player_rps}")
        print(f"computer: {computer_rps}")
        print("round {} player wins".format(round))
        player += 1
        print("{1} : {0}".format(computer, player))
    elif player_rps == "scissors" and computer_rps == "rock":
        print(f"player: {player_rps}")
        print(f"computer: {computer_rps}")
        print("round {} computer wins".format(round))
        computer += 1
        print("{1} : {0}".format(computer, player))
    elif player_rps == "scissors" and computer_rps == "paper":
        print(f"player: {player_rps}")
        print(f"computer: {computer_rps}")
        print("round {} player wins".format(round))
        player += 1
        print("{1} : {0}".format(computer, player))

#win announcer
if player_rps == 2:
    print("player wins")
elif computer_rps == 2:
    print("computer wins")
