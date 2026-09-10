Name = input("Please Input Your Name:  ")
print("-----------------------------------------------------")
item_type = input("What is the type of items:  "  )
print("-----------------------------------------------------")
fragile = bool(input("is it fragile? True or False?  "  ))
print("-----------------------------------------------------")
weight = float(input("How heavy is it?  "  ))
print("-----------------------------------------------------")
distance = float(input("How far do it need to travel?  "  ))
print("-----------------------------------------------------")
express = bool(input("Is it rushed?  True or False?  "  ))
print("-----------------------------------------------------")
international = bool(input("is it international? True or False?  "  ))
print("-----------------------------------------------------")


base_cost = (weight * 2.50) + (distance * 0.15)


# Free Shipping
if weight <= 2 and distance <= 100 and express == False and international == False:
	print(" Free Shipping  ")
	output = 0

# International
elif express == True and international == True:
	print("express and international is applied")
	output = (base_cost * 1.40) + 50

# Express of Heavy International
elif express == True or international == True and weight >= 20 and weight <=29.9:
	print("Heavy and Express/International applied") 
	output = (base_cost * 1.20) + 25

# Oversized
elif weight >= 30 or distance > 1000:
	print("Oversized package is applied")
	output = base_cost + 30

else:
	print(" based cost ")
	output = base_cost

print("Your total amount is", output)

# There's a problem, when you type false on the it becomes true. but when you enter it becomes false
