fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
    
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From:"):
        continue
    ls = line.split()
    ls =  line[5:]
    count = count + 1
    print(ls.strip())
        

print("There were", count, "lines in the file with From as the first word")

