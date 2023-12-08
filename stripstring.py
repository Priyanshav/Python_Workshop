s = "           Hello"
print(s.strip())
#lstrip() and rstrip()
print(s.rstrip())
print(s.lstrip())
n = "Priyanshu Kumar\n"
print(n * 3)
print(n + 'Chaudhary')
print(len(n))
print(n.find('u'))
print(n.count('u'))
print(n.lower())
print(n.upper())
print(n.replace('u', 'av'))
print(n.startswith('P'))
print(n.startswith('K'))
p = "lauresh gand"
print(p.capitalize())
print(p.title())
print(p.islower())
print(p.isupper())
print(p.isdigit())
print(p.isalpha())


s1 = "1,2,3,4,6"
ls = s1.split(",")
print(ls)
print("-".join(ls))
print(p.isspace())