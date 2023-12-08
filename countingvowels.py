s = input("Enter a string: ")
v,c = 0,0
for i in s.lower():
    if i in ['a','e','i','o','u']:
        v+=1
    elif i=='':
        continue
    else:
        c+=1
        
print("Vowels : {}\nConsonants:{}".format(v,c))