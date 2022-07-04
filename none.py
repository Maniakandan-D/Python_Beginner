shopping_list = ["milk", "eggs", "bread", "rice", "oil"]

item_to_find = input("What do you want in the Shopping_list: ")
found_at = None  # None is a constant used to show something doesn't have value

# for index in range(5)
# for index in range(len(shopping_list)):
#    if shopping_list[index] == item_to_find:
#        found_at = index
#        break  # break cause python is jump out the loop
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
