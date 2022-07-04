answer = 10

print("Please guess number between 1 to 10: ")
guess = int(input("Please enter the guess: "))

if guess < answer:
    print("Please guess higher")
    guess = int(input("Enter the second guess: "))
    if guess == answer:
        print("well done, you guessed it")
    else:
        print("Sorry, you guessed not correctly")
elif guess > answer:
    print("Please guess Lower ")
    guess = int(input("Enter the second guess: "))
    if guess == answer:
        print("well done, you guessed it")
    else:
        print("Sorry, you guessed not correctly")
else:
    print("you got it first time ")
