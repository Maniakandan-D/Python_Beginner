parrot = "Norwegian blue"

letter = input("Please enter a letter: ")

if letter in parrot:
    print("{} is an {}".format(letter, parrot))  # {} replace letter and parrot
else:
    print(" I don't need that letter")
