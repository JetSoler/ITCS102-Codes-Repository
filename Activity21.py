sum = 0
tuloy = True

while tuloy == True:
    x = int(input("Please enter your number  "))
    if x == 0:
        print("Loop Terminated")
        break
    else:
        print("Continue loop")
        sum += x
        print("Current total is ", sum)
        continue