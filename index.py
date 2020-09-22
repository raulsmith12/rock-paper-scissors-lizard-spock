from random import randint

#List of playable options
t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

#assigning a random interval play to the computer
computer = t[randint(0,4)]

#set player to false
player = False

while player == False:
#setting player to True
    player = input("Rock, Paper, Scissors, Lizard, Spock? --> ")
    if player == computer:
        print("Tie! Let's play again!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        elif computer == "Spock":
            print("You lose!", computer, "vaporizes", player)
        else:
            print("You win!", player, "crushes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        elif computer == "Lizard":
            print("You lose!", computer, "eats", player)
        elif computer == "Spock":
            print("You win!", player, "disproves", computer)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "crushes", player)
        elif computer == "Spock":
            print("You lose!", computer, "smashes", player)
        elif computer == "Lizard":
            print("You win!", player, "decapitates", computer)
        else:
            print("You win!", player, "cuts", computer)
    elif player == "Lizard":
        if computer == "Rock":
            print("You lose!", computer, "crushes", player)
        elif computer == "Scissors":
            print("You lose!", computer, "decapitates", player)
        elif computer == "Spock":
            print("You win!", player, "poisons", computer)
        else:
            print("You win!", player, "eats", computer)
    elif player == "Spock":
        if computer == "Paper":
            print("You lose!", computer, "disproves", player)
        elif computer == "Lizard":
            print("You lose!", computer, "poisons", player)
        elif computer == "Scissors":
            print("You win!", player, "smashes", computer)
        else:
            print("You win!", player, "vaporizes", computer)
    else:
        print("Invalid play. Please check your spelling or choses one of the options and try again.")

    player = False
    computer = t[randint(0,4)]
