class Stack:
    def __init__(self):
        self.stack = []

    # append func to push
    def push(self, data):
        self.stack.append(data)

    # remove
    def pop(self):
        self.stack.pop()

    # print data in element
    def traversal(self):
        for data in self.stack:
            print(data)


data_1 = Stack()
# data to check
data_1.push(10)
data_1.push(20)
data_1.push(30)
data_1.push(40)
# remove the list
data_1.pop()
# all element
data_1.traversal()
