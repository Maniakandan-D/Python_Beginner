computer_parts = ["computer",
                  "mouse",
                  "keyboard",
                  "cpu",
                  "mouse mat",
                  "monitor"
                  ]
print(computer_parts)

#computer_parts[3] = "dvd player"  # index position 3 (cpu) is replace
print(computer_parts[3:])

computer_parts[3:] = ["dvd player"]
print(computer_parts)