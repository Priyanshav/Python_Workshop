d = {'a':100, 'b':800, 'c':"python"}
print(d['b'])
#get method
print(d.get('b'))
d['d'] = "C++"
d['e'] = "Google Go"
#update method
d.update({'f':790, 'g':10000})
print(d)