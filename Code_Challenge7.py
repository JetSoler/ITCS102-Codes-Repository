n = int(input("Enter a number: "))

for x in range(n):
    d = abs(x - n // 2)
    for y in range(n):
        if y >= d and y <= n - 1 - d and (y - d) % 2 == 0:
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()
