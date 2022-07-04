shopping_list = ["milk", "eggs", "bread", "rice", "oil"]

# for item in shopping_list:
#   if item != "eggs":
#        print("Buy " + item)
for item in shopping_list:
    if item == "eggs":
        continue
    print("Buy " + item)
