# To crate Full Pyramid in using *
num = int(input("Enter the number of rows: "))
a = 0
for i in range(1, num + 1):
    # outermost loop start from i=1 to num+1= i
    for space in range(1, (num - i) + 1):
        # (num-i)+1 using for total number of rows i is current row
        print(end=" ")
    while a != (2 * i - 1):
        # (2*i-1) is using for number of stars in each rows ,the row is i
        print('*', end=" ")
        a += 1

    a = 0
    print()
