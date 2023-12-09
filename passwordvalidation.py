st = input("Enter the password: ")
a,d,s = 0,0,0
for i in st:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        a+=1
    else:
        s+=1
        
if d>3 and a>5 and s>=2:
    print("Valid Password")
else:
    print("Not a Valid Password")