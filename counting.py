st = input("Enter a string: ")
d,s,a = 0,0,0
for char in st:
    if char.isdigit():
        d+=1
    elif char.isalpha():
        a+=1
    elif char.isspace():
        s+=1
        
print("Count of digits: ",d)
print("Count of alphabets: ",a)
print("Count of spaces: ",s)