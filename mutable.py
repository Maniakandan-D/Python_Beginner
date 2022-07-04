computer_parts = ["computer",
                  "mouse",
                  "keyboard",
                  "cpu",
                  "mouse mat",
                  ]
another_parts = computer_parts
print(id(computer_parts))
print(id(another_parts))

computer_parts += ["monitor"]
print(computer_parts)
print(id(computer_parts))

a = b = c = d = e = f = another_parts
print("adding camara")
print(a)
b.append("camara")
print(c)
print(d)

