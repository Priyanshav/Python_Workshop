#opening the file
myfile = open("data.txt",'r')

#reading the file
# st = myfile.read(26)
# print(st)

#Method2
for each in myfile:
    print(each)
    
myfile.close()