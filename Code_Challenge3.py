Name = input("Please Input Your Name:  ")

item_type = input("What is the type of items:  "  )

fragile = bool(input("is it fragile?  "  ))

weight = float(input("How heavy is it?  "  ))

distance = float(input("How far do it need to travel?  "  ))

express = bool(input("Is it rushed?  "  ))

international = bool(input("is it international?  "  ))

base_cost = 5
costW = weight * 2.50 
CostD = distance * 0.15
CostE = 

if weight <= 2 and distance <= 100:
	print(" Based Cost is free  ")
else:
	print(" DENIED ")





# This is the freeshipping
#if weight <= 2 and distance <= 100 and express == False and international == False:
	#print(" Your shipping fee is free " )
#else:
	#print("DENIED")

#weight <= 2
#distance <= 100
#express = False
#international = False