def multiply(x, y):  # name of function is multiply() # we can also define an inside parenthesis
    result = x * y
    return result


def is_palindrome(string):
    # backward = string[::-1]  # reverse the original string
    # return backward == string
    return string[::-1] == string


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1] == string
    return is_palindrome(string)


# word = input("Please enter a word to check: ")
# if is_palindrome(word.casefold()):  # word is argument
#    print("'{}' is a palindrome".format(word))
# else:
#    print("'{}' is not a palindrome".format(word))


answer = multiply(23, 2)
print(answer)
