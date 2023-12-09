myfile = open("data.txt",'r')

st = myfile.read()
print("length of the file: ",len(st))
myfile.close()