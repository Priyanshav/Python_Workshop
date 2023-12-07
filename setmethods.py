a = {1,4,2,5}
#add method
a.add(3)
print(a)
#update method
a.update({1000,100000,1000000})
print(a)
#del keyword - it will remove the set completely
# del a
# print(a)
#clear method - will clear the elements and return empty set
# a.clear()
# print(a)
#remove method
a.remove(4)
print(a)
#pop method
a.pop()
print(a)
#discard method will not raise the error if an element is not their in the set unlike remove method
a.discard(100000)
print(a)