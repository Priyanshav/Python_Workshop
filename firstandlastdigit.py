n = input("Enter a number:")
t = n

while(len(n) == 4):
    a = int(t[0])
    b = int(t[-1])
    if(a%2==0 and b%2==0):
        print("True")
    elif(a%2!=0 and b%2!=0):
        print("True")
    else:
        print("False")
else:
    print("Enter a valid 4 digit number: ")
# break
