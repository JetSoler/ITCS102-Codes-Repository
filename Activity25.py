# def = define

def taga_triangle(number):
    for x in range(number, 0, -1):
        for y in range(1, x+1):
            print("*", end=" ")
        print()

taga_triangle(5)
taga_triangle(10)

def sum(x,y):
    return x+y

print(sum(4,5))

def box(size):
    for x in range(size+1):
        for y in range(size+1):
            if y == 0 or x == 0 or x == size or y == size:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

box(2)
box(5)

def my_myfactorial(number):
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact