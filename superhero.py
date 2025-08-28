# superhero.py

# This is the base class for all superheroes.
# It has a constructor (__init__) to initialize attributes.
class Superhero:
    """
    Represents a generic Superhero with a name, superpower, and secret identity.
    This class demonstrates constructors and attributes.
    """
    # The constructor is called when a new object is created.
    # It takes the name, superpower, and secret_identity as arguments.
    def __init__(self, name, superpower, secret_identity):
        # Attributes are variables that store data for each object.
        self.name = name
        self.superpower = superpower
        self.secret_identity = secret_identity
        self.is_good = True  # A default attribute for all superheroes.

    # This is a method (a function inside a class) that describes an action.
    def use_superpower(self):
        """Prints a message about the superhero using their main superpower."""
        print(f"{self.name} uses their {self.superpower} to save the day!")

    # Another method to reveal the hero's identity.
    def reveal_identity(self):
        """Reveals the superhero's secret identity."""
        print(f"I am... {self.secret_identity}!")


# This is a child class that inherits from the Superhero class.
# It gets all the attributes and methods of Superhero.
class FlyingSuperhero(Superhero):
    """
    Represents a Superhero that has the specific ability to fly.
    This class demonstrates inheritance and polymorphism.
    """
    # This constructor overrides the parent's but also calls it using `super()`.
    def __init__(self, name, superpower, secret_identity, flight_speed):
        # `super()` calls the constructor of the parent class (Superhero).
        super().__init__(name, superpower, secret_identity)
        # This is a new, specific attribute for flying superheroes.
        self.flight_speed = flight_speed

    # This method is a form of polymorphism.
    # It has the same name as the parent's method but a different implementation.
    def use_superpower(self):
        """Prints a more specific message about the superhero's superpower."""
        print(f"{self.name} soars through the sky at {self.flight_speed} mph!")
