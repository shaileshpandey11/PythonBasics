numbers = [1, 2, 3]

file = open("list.txt", "w")

for i in numbers:
    file.write(str(i)+"\n")

file.close()


