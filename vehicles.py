# vehicles.py

# This is the base class for all vehicles.
class Vehicle:
    """
    A base class for different types of vehicles.
    It defines a common method `move()` that will be implemented differently
    in its subclasses, which is a key part of polymorphism.
    """
    def __init__(self, make, model):
        # Common attributes for all vehicles.
        self.make = make
        self.model = model

    # This method is designed to be overridden by child classes.
    def move(self):
        """A placeholder for the move action."""
        raise NotImplementedError("Subclass must implement abstract method.")


# A child class that inherits from Vehicle.
class Car(Vehicle):
    """Represents a car, a type of vehicle."""
    # This method overrides the parent's `move` method.
    def move(self):
        """Defines how a car moves."""
        print(f"The {self.make} {self.model} is driving on the road. 🚗")


# Another child class that inherits from Vehicle.
class Plane(Vehicle):
    """Represents a plane, a type of vehicle."""
    # This method also overrides the parent's `move` method.
    def move(self):
        """Defines how a plane moves."""
        print(f"The {self.make} {self.model} is flying through the sky! ✈️")


# A third child class that inherits from Vehicle.
class Boat(Vehicle):
    """Represents a boat, a type of vehicle."""
    # This method also overrides the parent's `move` method.
    def move(self):
        """Defines how a boat moves."""
        print(f"The {self.make} {self.model} is sailing on the water. ⛵")
