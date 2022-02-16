from os import system
from random import choice
from time import sleep

class MainCharacter:

    def __init__(self, names, health, equipment):
        self.names = names
        self.health = int(health)
        self.equipment = []

    def reduce_health(self, amount):
        self.health -= amount

    def add_health(self, amount):
        self.health += amount

    def add_equipment(self, item):
        self.equipment.append(item)

#Scream
def scream():
    system('cls')
    print("You scream as loud as you can.")
    sleep(3)
    print("The sounds of your scream bounce around the room but to no avail.")
    sleep(3)
    print("Your voice starts rasping due to the dry atmosphere of the room.")
    sleep(3)
    print("Sweat beads down your forehead as you start to panic a little.")
    sleep(3)
    print("You hear a noise coming from beyond the door.")
    sleep(3)
    print("Quickly, you press your ear up against the wooden door.")
    sleep(3)
    choice = int(input("What will you do?\n[0] Yell for help\n[1] Look around the room, maybe you missed something\n[2] Try breaking down the door again, it's only wood\n:"))
    if choice == 0:
        print("You chose to yell for help")
    elif choice == 1:
        print("You chose look around the room")
    elif choice == 2:
        print("You chose to try and break the door down")

#Looking around
def look_around():
    system('cls')
    print("Examining the room, you notice that the rug is the only thing in the room.")
    sleep(3)
    print("The rug itself is ugly and old, but also has some weight to it.")
    sleep(3)
    print("You grab an end of the rug and pull as hard as you can.")
    sleep(3)
    print("This revealed what looks like a secret hatch")
    sleep(3)
    print("As you lay the rest of the rug down, you hear a very quiet snicker.")
    sleep(3)
    decision = int(input("What will you do?\n[0] Keep calm and open the hatch\n[1] Look around again to make sure you didn't miss anything\n[2] Scream\n:"))
    system('cls')
    if decision == 0:
        print("You chose to push forward and open the hatch")
    elif decision == 1:
        print("You chose to look around again.")
    elif decision == 2:
        print("You chose to scream")
    


#Breaking the door down
def break_door():
    system('cls')
    mc.reduce_health(1)
    sleep(3)
    print("You hurt your arm trying to break the door down.")
    sleep(3)
    print(f"Your health is {mc.health} HP")
    sleep(3)
    print("The door won't budge either.")
    sleep(3)
    print("Will you try again or look for more options?")
    sleep(3)
    choice = int(input("What will you do?\n[0] Try breaking the door down again\n[1] Look around the room, there's bound to be something of interest\n[2] You could try screaming\n:"))
    system('cls')
    if choice == 0:
        print("You have chosen to try again.")
        break_door()
    elif choice == 1:
        print("You have chosen to look around")
    elif choice == 2:
        print("You have chosen to scream")

def continue_game():
    input("Press Enter to Continue...")
    system('cls')

#Start the journey
def main():
    choice = int(input("What will you do?\n[0] Break down the door\n[1] Look around\n[2] Scream\n:"))
    if choice == 0:
        print("You chose to try and break the door")
        break_door()
    elif choice == 1:
        print("You chose to look around")
        look_around()
    elif choice == 2:
        print("You chose to scream")
        scream()

# Game Over
def game_over():
    system('cls')
    print("You have died")
    print("Would you like to restart?")
# Introduction and character definition

# Waking up
name = input("Before we get started, what is your name?\n:")
mc = MainCharacter(name, health=10, equipment=[])

while mc.health > 0:
    system('cls')
    print("You wake up")
    sleep(2)
    print("Confused...")
    sleep(2)
    print("Who am I?")
    continue_game()
    sleep(2)
    print(f"{mc.names}? Oh yeah...")
    sleep(2)
    print("How did I end up here? Where am I? Why is it so dark?")
    sleep(2)
    continue_game()
    print("The room is dark, but you can tell you're in a house.")
    sleep(2)
# Receiving heart monitor
    print("You check the floor and find some kind of device with a needle under a rug")
    sleep(2)
    print("This appears to be a health monitor to track my heart rate")
    sleep(2)
    continue_game()
    health_monitor = "Health Monitor"
    mc.add_equipment(health_monitor)
    print("You check your health.")
    sleep(2)
    print(f"You have {mc.health} HP")
    sleep(2)

# Puts device in inventory
    print("You stick the device in your pockets. This thing could be handy.")
    sleep(2)
    print(mc.equipment)
# End of character creation
    print("You look around the dim room and find a door")
    sleep(2)
    print("You try to open the door, but the handle won't move. The door appears to be locked.")
    continue_game()

    main()
else:
    game_over()
