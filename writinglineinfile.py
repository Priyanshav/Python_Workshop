m2 = open("data_to_write.txt", 'w')

ls = ["This is so good", "Noida ist laut", "Ich komme aus Indien"]
m2.writelines(ls)

m2.close()