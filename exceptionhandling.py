n = int(input("N: "))
y = int(input("Y: "))
try:
    z = n/y
    print(z)
except ZeroDivisionError:
    print("The error occured, check the divisor")
except NameError:
    print("Its a nameerror")
finally:
    print("Always executing")