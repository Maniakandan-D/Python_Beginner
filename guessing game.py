answer = 10

print("Please guess number between 1 to 10: ")
guess = int(input("Please enter the number: "))

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess Lower ")
else:
    print("you got it first time ")
