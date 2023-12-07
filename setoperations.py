s1 = {1,2,3,9,10}
s2 = {2,3,18,19}
#union method
# print(s1.union(s2))

#intersection method
# print(s1.intersection(s2))

#intersection_update method
# s1.intersection_update(s2)
# print(s1)

#difference method
# print(s1.difference(s2))
# print(s2.difference(s1))
print(s1)
# s1.difference_update(s2)
# print(s1)
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)