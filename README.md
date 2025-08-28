# python-oop-assignment
Python OOP Assignment
This project demonstrates core principles of Object-Oriented Programming (OOP) in Python, including classes, inheritance, and polymorphism.

The code is divided into three files:

main.py: The primary script that runs the demos for both assignments.

superhero.py: Contains the Superhero base class and the FlyingSuperhero subclass, demonstrating inheritance and method overriding.

vehicles.py: Contains the Vehicle base class and several subclasses (Car, Plane, Boat), demonstrating polymorphism through a common move() method.

Project Structure
.
├── main.py
├── superhero.py
└── vehicles.py

How to Run the Demos
Ensure all three files (main.py, superhero.py, and vehicles.py) are in the same folder.

Open a terminal or command prompt.

Navigate to the directory where the files are located.

Run the main.py script using the Python interpreter:

python main.py

Assignment 1: Superhero Class Demo
This section of the code in main.py creates instances of the Superhero and FlyingSuperhero classes to show how a child class inherits attributes and methods from a parent class.

Assignment 2: Polymorphism Demo
This part of the script creates a list of different Vehicle objects (Car, Plane, and Boat). It then loops through the list and calls the move() method on each object. Because of polymorphism, each object executes its own specific version of the move() method.
