def centre_text(*args, sep=' '):  # , end='\n', file=None, flush=False
    text = ""
    for arg in args:
        text += str(arg) + sep
    text = str(text)  # str function to convert the argument that was passed to a string
    left_margin = (80 - len(text)) // 2  # center of text
    return " " * left_margin + text
    # print(" " * left_margin, text, end=end, file=file, flush=flush)


# with open("centred", mode='w') as centre_file:
# call the function
#    centre_text("spam and egs", file=centre_file)
#    centre_text("spam, spam and eggs", file=centre_file)
#    centre_text(12, file=centre_file)  # integer get converted to string
#    centre_text("spam, spam, spam and spam", file=centre_file)
#    centre_text("first", "second", 3, 4, "five", sep=":", file=centre_file)
# creating function that allows to text to be printed centered on the screen
# there is no flush parameter
# s1 = centre_text("spam and egs")
# print(s1)
# s2 = centre_text("spam, spam and eggs")
# print(s2)
# s3 = centre_text(12)
# print(s3)
# s4 = centre_text("spam, spam, spam and spam")
# print(s4)
# s5 = centre_text("first", "second", 3, 4, "five", sep=":")
# print(s5)
with open("menu", 'w') as menu:

    s1 = centre_text("spam and egs")
    print(s1, file=menu)
    s2 = centre_text("spam, spam and eggs")
    print(s2, file=menu)
    s3 = centre_text(12)
    print(s3, file=menu)
    s4 = centre_text("spam, spam, spam and spam")
    print(s4, file=menu)
    s5 = centre_text("first", "second", 3, 4, "five", sep=":")
    print(s5, file=menu)
