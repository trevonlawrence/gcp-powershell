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
    print("You scream as loud as you can.")
    print("The sounds of your scream bounce around the room but to no avail.")
    print("Your voice starts rasping due to the dry atmosphere of the room.")
    print("Sweat beads down your forehead as you start to panic a little.")
    print("You hear a noise coming from beyond the door.")
    print("Quickly, you press your ear up against the wooden door.")
    choice = int(input("What will you do?\n[0] Yell for help\n[1] Look around the room, maybe you missed something\n[2] Try breaking down the door again, it's only wood\n:"))
    if choice == 0:
        print("You chose to yell for help")
    elif choice == 1:
        print("You chose look around the room")
    elif choice == 2:
        print("You chose to try and break the door down")

#Looking around
def look_around():
    print("Examining the room, you notice that the rug is the only thing in the room.")
    print("The rug itself is ugly and old, but also has some weight to it.")
    print("You grab an end of the rug and pull as hard as you can.")
    print("This revealed what looks like a secret hatch")
    print("As you lay the rest of the rug down, you hear a very quiet snicker.")
    decision = int(input("What will you do?\n[0] Keep calm and open the hatch\n[1] Look around again to make sure you didn't miss anything\n[2] Scream\n:"))
    if decision == 0:
        print("You chose to push forward and open the hatch")
    elif decision == 1:
        print("You chose to look around again.")
    elif decision == 2:
        print("You chose to scream")
    


#Breaking the door down
def break_door():
    mc.reduce_health(1)
    print("You hurt your arm trying to break the door down.")
    print(f"Your health is {mc.health}")
    print("The door won't budge either.")
    print("Will you try again or look for more options?")
    choice = int(input("What will you do?"))
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
# Introduction and character definition

# Waking up
system('cls')
print("You wake up")
sleep(2)
print("Confused...")
sleep(2)
print("Who am I?")
sleep(2)
continue_game()
name = input("What's my first name?\n:")
system('cls')
mc = MainCharacter(name, health=10, equipment=[])
sleep(2)
print(f"{mc.names}? Oh yeah...")
sleep(2)
print("How did I end up here? Where am I? Why is it so dark?")
sleep(2)
continue_game()
print(f"You check your pockets and find...\n{mc.equipment}")
sleep(2)
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