f = open("p022_names.txt")
names = f.read()[1:-1].split('","')
names.sort()
name_sum = 0
for i in range(len(names)):
    name = names[i]
    name_sum += (i+1)*sum([ord(char)-64 for char in name])


print(name_sum)
