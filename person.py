class person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def intro(self):
        print("my name is " + self.name)


r1 = person('mani', 'good', True)  # variable name.class name (init method answer)
r1.intro()  # variable.function name
