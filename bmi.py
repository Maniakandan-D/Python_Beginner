def bmi(name, height_m, weight_kg):
    bmi_cal = weight_kg / (height_m ** 2)
    print("Bmi: ")
    if bmi_cal < 25:
        # return name + " is not over weight"
        print("{} is not over weight".format(name))
    else:
        print("{} is over weight".format(name))


# a = bmi(name='mani', height_m=2, weight_kg=60)
bmi(name='mani', height_m=2, weight_kg=60)
