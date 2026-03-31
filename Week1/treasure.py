print("Welcome to The Antivan Treasury!")
print("Your mission is to find the Antivan Treasury!")

hallway = input(
    "You open a door that leads into a hallway. Which way do you go? "
    "Type 'Left' or 'Right'\n "
).lower()

if hallway == "right":
    stairs = input(
        "Clear! At the end of the hallway is a set of stairs. "
        "One going up, the other going down. "
        "Type 'Up' or 'Down'\n "
    ).lower()

    if stairs == "up":
        doors = input(
            "You see three doors. "
            "One has a Dragon, one has a Griffin, and one has a Crow. "
            "Which do you choose? Type 'Dragon' or 'Griffin' or 'Crow'\n "
        ).lower()

        if doors == "dragon":
            print("Better luck next time!")
        elif doors == "griffin":
            print("So close!")
        elif doors == "crow":
            print("Welcome to the Crows, Fledgling!")
        else:
            print("Sorry, I don't know what you're doing!")

    elif stairs == "down":
        print("You tripped on Viago's poisonous plants! Hurry to the Healers!")
    else:
        print("Sorry, I don't know what you're doing!")

elif hallway == "left":
    print("Spotted by Teia! You need more training!")
else:
    print("Sorry, I don't know what you're doing!")