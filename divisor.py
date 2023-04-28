#This programs asks the user for a number then prints out all the divisors for this number between 1-100#
num = int(input("Enter a number: "))
x = range(1, 100)
for y in x:
    if (num % y) == 0:
        print(y)
        