# jabber = open("sample.txt",'r')
# # jabber = open("C:\\Documents and Settings\\tim\\My Documents\\sample.txt", 'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()

# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
#
# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')
#

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')
for line in reversed(lines):
    print(line, end= " ")
# line stop summer's reach
with open('sonnet.txt') as sonnet:
    while True:
        text = sonnet.readline().rstrip() # strip line before binding a variable line to it
        print(text)
        if "summer's" in text.casefold():
            break

print("*" * 80)
with open('sonnet.txt') as sonnet:
    for text in sonnet:
        print(text.rstrip())   # strip the new line only for printing
        # a string contain a new line string are immutable
        if "summer's" in text.casefold():
            break


a = open('sonnet.txt')






