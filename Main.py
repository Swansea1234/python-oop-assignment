# main.py

# Import the classes from the other two files.
# If you are getting an error on the 'vehicles' word,
# make sure the file is named 'vehicles.py' and is in the same folder as this file.
from superhero import Superhero, FlyingSuperhero
from vehicles  import Car, Plane, Boat

# --- Assignment 1: Design a Class ---
print("--- Assignment 1: Superhero Class Demo ---")

# Create an instance of the base Superhero class.
classic_hero = Superhero("Captain Courage", "super strength", "Clark")
# Use its methods.
classic_hero.use_superpower()
classic_hero.reveal_identity()

print("-" * 20)

# Create an instance of the inherited class.
flying_hero = FlyingSuperhero("Skylark", "flight", "Lois", 500)
# This calls the overridden method from FlyingSuperhero.
flying_hero.use_superpower()
flying_hero.reveal_identity()

print("\n") # Add a blank line for better readability.

# --- Assignment 2: Polymorphism Challenge ---
print("--- Assignment 2: Polymorphism Demo ---")

# Create a list of different vehicle objects.
fleet = [
    Car("Ford", "Focus"),
    Plane("Boeing", "747"),
    Boat("Catalina", "30")
]

# Loop through the list and call the `move()` method on each object.
# Even though we are calling the same method name, each object
# knows how to execute it differently because of polymorphism.
for item in fleet:
    item.move()
