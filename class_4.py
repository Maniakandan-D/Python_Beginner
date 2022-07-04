class Dogs:
    animal = 'Dog'

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour


# object of dog
Cheetah = Dogs('PUG', 'white')
Mr_Black = Dogs('Bulldog', 'black')

print("Cheetah details:")
print("Cheetah is a ", Cheetah.animal)
print("Breed: ", Cheetah.breed)
print("Colour: ", Cheetah.colour)
print()
print("Mr_Black details:")
print("Mr_Black is a ", Mr_Black.animal)
print("Breed: ", Mr_Black.breed)
print("Colour: ", Mr_Black.colour)
# class variable can be accessed using class name also
print("\nAccessing class variable using class name ")
print(Dogs.animal)
