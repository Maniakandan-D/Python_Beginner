available_parts = ["computer",
                   "monitor",
                   "mouse",
                   "keyboard"
                   ]
# valid_choice = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choice = []
for i in range(1, len(available_parts) + 1):
    valid_choice.append(str(i))
print(valid_choice)
current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choice:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in , so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add option to given list below:")
        for part in available_parts:
            print("{0}: {1}".format(available_parts.index(part) + 1, part))

    current_choice = input()
print(computer_parts)
