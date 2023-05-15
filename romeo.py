#This program will open a file, read it line by line. It will use the split() method to to create a list of the words, then search the list and make a seperate of 
fname = input("Enter file name: ")
fh = open(fname)
lst = []
for word in fh:
    x = word.split()
    for y in x:
        if y not in lst:
            lst.append(y)
lst.sort()
print(lst)
      
