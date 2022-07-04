pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)


numbers = [1.2, 7.8, 9.0, 2.3, 5.6, 1.1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumps over the lazy dog", key=str.casefold)  # case insensitive
print(missing_letter)

names = ["Mani",
         "gowtham",
         "dhilip",
         "ashwin"
         ]
names.sort(key=str.casefold)
print(names)
