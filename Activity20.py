from getpass import getpass

u = "Jet"
p = "Hatdog1"

isLogin = False
while isLogin == False:

    user = input("please put your username ---->>  ")
    pword = getpass("Please input your password----->>  ")

    if user == u and pword == p:
        print("LOG IN SUCCESSFUL")
        isLogin = True
    else:
        print("LOG IN FAILED")
        isLogin = False