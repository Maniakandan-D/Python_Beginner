vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier can-Am 250',
    'virago': 'Yamaha XT650',
    'tenere': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4'
}

vehicles["starfighter"] = "lockheed F-104"
vehicles["toy"] = "glider"
# upgrade virago
vehicles["virago"] = "Yamaha XV345"

del vehicles["virago"]

# my_car = vehicle['roadster']  # retrieve the value
# print(my_car)

# commuter = vehicle['virago']
# print(commuter)
# another way
# learner = vehicle.get("er5") # key is get method
# print(learner)

# for key in vehicle: # iterating over the key
#    print(key)
#    print(key, vehicle[key], sep=",")

for key, value in vehicles.items():
    print(key, value, sep=",")
