animals = {
    'Turtle',
    'Horse',
    'Robin',
    'python',
    'Swallow',
    'Hedgehog',
    'wren',
    'Aardvark',
    'cat',
}
birds = {'Robin', 'Swallow', 'wren'}

print(f'birds is a subset of animals:{birds.issubset(animals)}')
print(f'animals is a superset of birds:{animals.issuperset(birds)}')
print()

print(birds < animals)    # to check proper superset
print(animals >= birds)    # to check animals is a superset of birds
print("*" * 80)
garden_birds = {'wren', 'Swallow', 'Robin'}
print(birds == garden_birds)
