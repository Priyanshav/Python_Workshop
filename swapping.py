a,b = 10,20

print(f"Before swap: a = {a}, b = {b}")
#method-1
temp = a
a = b
b = temp
#method-2
# a = a+b #a = 10+20 = 30
# b = a-b #b = 30-20 = 10
# a = a-b #a = 30-10 = 20
print("after swap: a = {}, b = {}".format(a,b))
# method-3
print("after swap: a = {1}, b = {0}".format(a,b))