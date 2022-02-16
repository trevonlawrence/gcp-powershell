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

    def get_equipment(self):
        print(self.equipment)

    def add_equipment(self, item):
        self.equipment.append(item)

#Health Mechanics        
def health_mechanic_checker():
    print("Let's see if you can take damage")
    mc.reduce_health(1)
    print(mc.health)
    print("Good, I will restore your health")
    mc.add_health(1)
    print("Let's make sure that worked")
    print(mc.health)

#Start the journey
def main():
    choice = int(input("What will you do?"))
    if choice == 0:
        print("You chose to try and break the door")
        break_door()
    elif choice == 1:
        print("You chose to look around")
    elif choice == 2:
        print("You chose to scream")
    
#Breaking the door down
def break_door():
    mc.reduce_health(1)
    print("You hurt your arm trying to break the door down.")
    print(mc.health)
    print("The door won't budge either.")
    print("Will you try again or look for more options?")
    choice = choice = int(input("What will you do?"))
    if choice == 0:
        print("You have chosen to try again.")
        break_door()
    elif choice == 1:
        print("You have chosen to look around")
    elif choice == 2:
        print("You have chosen to scream")

#Introduction and character definition

print("You wake up")
#sleep(2)
print("Confused...")
#sleep(5)
print("Who am I?")
name = input("What's my first name?")
mc = MainCharacter(name, health=10, equipment=[])
#sleep(5)
print(f"{mc.names}? Oh yeah...")
#sleep(2)
print("How did I end up here? Where am I? Why is it so dark?")
#sleep(2)
check_equipment = mc.get_equipment()
print(f"You check your pockets and find...\n{check_equipment}")
#sleep(2)
print("The room is dark, but you can tell you're in a house.")
print("You check the floor and find some kind of device with a needle under a rug")
print("This appears to be a health monitor to track my heart rate")
health_monitor = "Health Monitor"
mc.add_equipment(health_monitor)
print(mc.equipment)
print("Let's check the health mechanics.")
health_mechanic_checker()
print(f"Your health right now is {mc.health} HP")
print("You look around the dim room and find a door")
print("You try to open the door, but the handle won't move. The door appears to be locked.")

main()