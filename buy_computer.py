available_parts = ["computer",
                   "monitor",
                   "mouse",
                   "keyboard",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive",
                   ]
#  valid_choice = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choice = []
for i in range(1, len(available_parts) + 1):
    valid_choice.append(str(i))
print(valid_choice)
current_choice = "-"
computer_parts = []  # create an empty list

while current_choice != '0':
    if current_choice in valid_choice:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
        # if current_choice == "1":
        #   computer_parts.append("computer")
        # elif current_choice == "2":
        #    computer_parts.append("monitor")
        # elif current_choice == "3":
        #   computer_parts.append("mouse")
        # elif current_choice == "4":
        #    computer_parts.append("keyboard")
        # elif current_choice == "5":
        #    computer_parts.append("mouse mat")
        # elif current_choice == "6":
        #    computer_parts.append("hdmi cable")
    else:
        print("Please add option to list below:")
        for part in available_parts:
            print("{0}: {1}".format(available_parts.index(part) + 1, part))

    current_choice = input()
print(computer_parts)
