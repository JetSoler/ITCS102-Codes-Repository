# Variables:
Money = int(input("input money --->>  "))
a = 1000
b = 500
c = 200
d = 100
e = 50
f = 20
g = 10
h = 5
i = 1
bal = Money

# This if for the account balance
print("Balance =", bal)

# This is for the 1000
print("1000 =", Money//a)

# This is for the 500
print("500 =", bal//b)
bal %= b

# This is for the 200
print("200 =", bal//c)
bal %= c

# This is for the 100
print("100 =", bal//d)
bal %= d

# This is for the 50
print("50 =", bal//e)
bal %= e

# This is for the 20
print("20 =", bal//f)
bal %= f

# This is for the 10
print("10 =", bal//g)
bal %= g

# This is for the 5
print("5 =", bal//h)
bal %= h

# This is for the 1
print("1 =", bal//i)
bal %= i
