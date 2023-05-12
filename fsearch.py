#This program will prompt the user for a file name, then open and reads the file looking for a specific item.
total = float(0)
count = 0
fname = input("Enter file name: ")
fh = open(fname, 'r')
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ls = line.split()
    count = count + 1
    total += float(ls[1])
    #b = []
    #b.append(float(line[20:26]))
    
print("Average spam confidence:", total/count)    
#total = total + float(b)
#print("Average spam confidence:", total/count)
