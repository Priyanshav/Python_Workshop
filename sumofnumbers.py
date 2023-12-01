n = int(input("Enter a number: "))
t = n
s = 1
while(t>0):
    rem = t%10
    s *= rem
    t //= 10
    
print("Product of individual digits is: ",s)