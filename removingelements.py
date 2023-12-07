ls = list(map(int,input("Enter list: ").split()))
l =[]

for i in ls:
    if i not in l:
        l.append(i)
        
print(l)