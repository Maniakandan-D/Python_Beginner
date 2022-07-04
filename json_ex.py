import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

# with open('test.json', 'w', encoding='utf-8') as testfile:
# The dump function serialise the data we give it, and write the result to the file
#    json.dump(languages, testfile)

with open('test.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)  # load command to read the data from the file and decode it
print(data)
print(data[3])
