adventure_exist = ["south", "east", "north", "west"]
chosen_exist = ""

while chosen_exist not in adventure_exist:
    chosen_exist = input("Please Enter the direction: ")
    if chosen_exist.casefold() == "quit":
        print("Game over")
        break

print("aren't you glad you got out of there")
