#This program will create a dictionary with the conditions that if a name is in the dictionary add 1 to the count. If the name is not in the dictionary it will add the name to the dictionary and add one to the count for it.

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] =counts[name]+1
print(counts)
