name = input("Type your name: ")
print("Welcome to the adventure,", name, "!")

answer = input(
    "You have arrived at the Firelink Shrine. Do you continue down the path to the right, or do you go left?: ").lower()

if answer == "left":
    answer = input("You've reached the High Wall of Lothric, where there are two cathedrals - one is at the bottom of a hill, the other at the top. Type 'bottom' to travel to the cathedral at the bottom, type 'top' to travel to the cathedral at the top: ").lower()

    if answer == "bottom":
        print("You enter a decrepit cathedral housing a giant armored creature named Vordt of the Boreal Valley. Vordt lets out a massive scream that shakes the cathedral walls, causing you to lose your footing as he jumps towards you and swings his frozen mace. YOU DIED.")

    elif answer == "top":
        answer = input("Inside the cathedral at the top, there is a frail elderly person on the floor at the altar uttering nonsense. Type 'slay' to slay the stranger with your sword and put them out of their misery, or 'leave' to walk away and enter the other cathedral down the hill: ").lower()

        if answer == "slay":
            print("You have mudered an innocent NPC, which caused the Dancer of the Boreal Valley to spawn and attack you. You try to fight back, but resistance is futile. YOU DIED.")
        elif answer == "leave":
            print("You enter a decrepit cathedral housing a giant armored creature named Vordt of the Boreal Valley. Vordt lets out a massive scream that shakes the cathedral walls, causing you to lose your footing as he jumps towards you and swings his frozen mace. YOU DIED.")
        else:
            print("Invalid option. You rolled off a cliff. YOU DIED.")

    else:
        print("Invalid option. You rolled off a cliff. YOU DIED.")

elif answer == "right":
    answer = input("You've arrived at the Undead Settlement, which is filled with pitch-fork wielding zombies. Type 'fight' to fight through the zombies, or 'run' to try and get past them all: ").lower()

    if answer == "fight":
        answer = input("You killed all of the zombies in the area, and arrive at a large open courtyard with a massive tree at the center. Type 'inspect' to take a closer look at the tree, or type 'leave' to run away and find another path: ").lower()
        if answer == "inspect":
            print("As you slowly step closer towards the tree and place your hand upon its trunk, the tree becomes alive and swings down on your with its branches. YOU DIED.")
        elif answer == "leave":
            print(
                "Whoops, there's a hole in the ground right behind you and you fell in. YOU DIED.")
        else:
            print("Invalid option. You rolled off a cliff. YOU DIED.")

    if answer == "run":
        print("OMG YOU DEFEAT THE SOUL OF CINDER AT THE KILN OF THE FIRST FLAME! YOU JUST BROKE THE SPEEDRUN RECORD! CONGRATULATIONS CHOSEN UNDEAD - YOU WIN!")


else:
    print("Invalid option. You rolled off a cliff. YOU DIED.")
