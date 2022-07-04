# instance variable inside method
class Dog:
    animal = 'dog'

    def __init__(self, breed):
        self.breed = breed  # instance variable

    def set_colour(self, colour):  # adds an instance variable
        self.colour = colour

    def get_colour(self):  # retrieves instance variable
        return self.colour


# driver code
Mani = Dog('m')
Mani.set_colour("Yellow")
print(Mani.get_colour())
