shopping_list = ["milk", "eggs", "bread", "rice", "oil"]

for item in shopping_list:
    if item == "eggs":
        break  # terminate after the break
    print("Buy " + item)
item_to_found = "eggs"
found_at = None  # None is a constant used to show something doesn't have value
#
# # for index in range(5)
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_found:
#         found_at = index
#         break  # break cause python is jump out the loop
# print("item found at position {}".format(found_at))
