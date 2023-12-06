str1 = input("Enter a input: ")
repo = "abcdefghijklmnopqrstuvwxyz"
str2 = ""
count = 0
for i in range(len(str1)):
    if str1[i] in repo:
        count += 1
        #continue
    else:
        str2 += str1[i]
        
print("Number of Alphabets",count)
print("String after removing alphabets: ",str2)