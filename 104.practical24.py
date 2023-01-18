weight = float(input("Enter the weight of the package in kg: "))
if weight <= 2:
    cost = weight * 25
elif weight > 2 and weight <= 6:
    cost = weight * 20
elif weight > 6 and weight <= 10:
    cost = weight * 15
elif 10 > weight < 50:
    cost = weight * 10
elif weight >= 50:
    print("The package cannot be shipped.")
    cost = None
    
if cost:
    print("The shipping cost is: ", cost, "Dhs")
