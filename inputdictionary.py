d = {}
n = int(input("Enter length of dict: "))
for i in range(1,n+1):
    key = input("Enter the key: ")
    value = input("Enter value: ")
    d[key] = value
    
print("Dictionary is: ",d)