#This program will prompt the user for a file name, then open and read the file. It will print the contents of fill in uppercase.

fname = input("Enter file name: ")
fh = open(fname, 'r')
for x in fh:
    x = x.strip()
    x = x.upper()
    print(x)
    
