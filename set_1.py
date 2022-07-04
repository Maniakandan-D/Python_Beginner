farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)
wild_animal = {'lion', 'horse', 'tiger', 'elephant', 'goat'}
print(wild_animal)

union = farm_animals.union(wild_animal)  # => farm_animals | wild_animal
print(union)
a = farm_animals ^ wild_animal  # => farm_animal.symmetric_difference(wild_animal)
print(a)
b = farm_animals - wild_animal  # => farm_animal.difference(wild_animal)
print(b)
c = farm_animals & wild_animal  # => farm_animal.intersection(wild_animal)
print(c)
