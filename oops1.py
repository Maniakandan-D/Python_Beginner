class Kettle(object):
    power_source = "electricity"  # class attribute

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("kenwood", 8.9)  # instance of class
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.5
print(kenwood.price)

hamilton = Kettle("hamilton", 10)  # another instance created
print(hamilton.make)
print(hamilton.price)
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
# created parameters in the formatted method
"""
class : template for creating objects. All objects created using the same class will have the same characteristics.
object : an instance of class
Instantiate : create a instance of class
Method : a variable bound to an instance of a class
Attributes : a variable bound to an instance of a class
"""

print(kenwood.power_source)
print(hamilton.power_source)

