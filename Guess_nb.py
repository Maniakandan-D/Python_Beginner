min = 0
max = 100
print("Please guess the number between {} to {}: ".format(min, max))
guesses = 1
while True:
    guess = min + (max - min) // 2  # formula
    answer = input("My guess is {} correct. Should i guess max or min ?"
                   " Enter x or y, or z if my guess was correct: ".format(guess)).casefold()  # case sensitive
    if answer == 'x':
        # The min end of the range becomes 1 greater than guess
        min = guess + 1
    elif answer == 'y':
        # The max end of the range becomes one less than guess
        max = guess - 1
    elif answer == 'z':
        print("You thought the number of {}".format(guess))
        print("I got it in {} guesses".format(guesses))
        break
    else:
        print("Please enter x, y or z")
    guesses += 1  # augmented assignment

