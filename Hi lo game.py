low = 1
high = 5000
print("Please think a number between {} and {}".format(low, high))
input("Please ENTER to START the game")

guesses = 1
# True
while low != high:
    # print("\tGuesses in the range of {} , {} ".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}.Should I guess higher or lower ?"
                     " Enter h or l, or c if my guess was correct: ".format(guess)).casefold()
    if high_low == "h":
        # Guess the higher .The low end of the range becomes 1 greater than guess
        low = guess + 1
    elif high_low == "l":
        # Guess the lower. The high end of the range becomes one less than guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses! ".format(guesses))
        print("I am genius you agree ?.... (:")
        break
    else:
        print("Please enter h , l or c")
    # guesses = guesses + 1
    guesses += 1
else:
    print("You thought the number of {}".format(low))
    print("I got it in {} guesses! ".format(guesses))
