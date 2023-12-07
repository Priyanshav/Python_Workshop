n = int(input("Enter a number to find factors: "))
# ls = [i for i in range (1,n+1) if n%i==0]
# print(*ls)

l = []
l.clear()
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
        
print(*l)   #* se comma aur bracket hat jaata hai