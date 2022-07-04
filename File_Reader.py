# raed write
class File_reader:

    def read_all_lines(self):
        with open('sonnet.txt', 'r') as sonnet:
            lines = sonnet.read()  # read all lines
            # lines = sonnet.readline() # read one line
            # lines = sonnet.readlines()  # list contains string
            print(lines)
            # line reversed
            # for line in reversed(lines):
            #     print(line, end="")

    def write_all_lines(self):
        cities = ["Chennai", "Bangalore", "Delhi", "Mumbai", "Hyderabad"]
        with open('cities.txt', 'w') as write:
            for city in cities:
                print(city, file=write)

    def append(self):
        cities = []
        with open('cities.txt', 'r') as write:
            for city in write:
                cities.append(city.strip('\n')) # remove \n
                print(cities)
                for city in cities:
                    print(city)


read = File_reader()
# read.read_all_lines()
# read.write_all_lines()
read.append()
