# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently 
# (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


# Base Class
class Animal:

    # The method that will be Polymorphised.
    def move(self):
        print(f"{self.__class__.__name__}: The animal moves.")


# Creating sub-classes to elaborate Polymorphism.

class Cat(Animal):
    def move(self):
        print(f"{self.__class__.__name__}: Cat-walks🐈🐈‍⬛..")

class Dog(Animal):
    def move(self):
        print(f"{self.__class__.__name__}: Running🐕..")

class Fish(Animal):
    def move(self):
        print(f"{self.__class__.__name__}: Swimming🐟🐠..")

class Bird(Animal):
    def move(self):
        print(f"{self.__class__.__name__}: Flying🦅🕊️..")

class Penguin(Animal):
    def move(self):
        print(f"{self.__class__.__name__}: Waddles🐧..")

class Lizard(Animal):
    def move(self):
        print(f"{self.__class__.__name__}: Crawling🦎..")

class Snake(Animal):
    def move(self):
        print(f"{self.__class__.__name__}:Creeping🐍..")


# Another Base Class
class Vehicle:
    def move(self):
        print(f"{self.__class__.__name__}: This vehicle moves.")

# Sub-classes to Polymorphize Vehicle Class.
class Car(Vehicle):
    def move(self):
        print(f"{self.__class__.__name__}: Driving 🚗")

class Boat(Vehicle):
    def move(self):
        print(f"{self.__class__.__name__}: Sailing 🚤")

class Plane(Vehicle):
    def move(self):
        print(f"{self.__class__.__name__}: Flying ✈️")


# Store each sub-classes in an array
move_action = [Bird(), Boat(), Car(), Cat(), Dog(), Fish(), Lizard(), Penguin(), Plane(), Snake()]

print(f"The total number of move_action is: {len(move_action)}.")
print()
# Iterate through and print out
for mover in move_action:
    mover.move()

print()
