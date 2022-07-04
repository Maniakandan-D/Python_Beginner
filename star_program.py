class Star:

    def star_fun(self:str):
        for i in range(0, self):
            for j in range(0, i + 1):  # each line
                print("*", end=' ')
                print(" ")
        for i in range(self + 1, 0, -1):
            for j in range(0, i - 1):  # decrease *
                print("*", end=' ')
                print(" ")


self = 3
if __name__ == '__main__':
    Star.star_fun(self)
