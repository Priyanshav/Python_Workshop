myfile = open("data.txt",'r+')

myfile.write("I am gonna be the KING of the Pirates!")

st = myfile.read()
print(st)
myfile.close()