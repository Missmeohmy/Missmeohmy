name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = 0
file = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    ls = line.split()
    thing = ls[1]
    file[thing] = file.get(thing, 0) + 1
bigcount = None
bigword = None
for thing,count in file.items():
    if bigcount is None or count > bigcount:
        bigword = thing
        bigcount = count

print(bigword, bigcount)