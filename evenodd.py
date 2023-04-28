x = int(input("Enter a number: "))
if (x % 2) == 0 and (x % 4) != 0:
    print("You rock!")
elif (x % 2) == 0 and (x % 4) == 0:
    print("Oh Snap")
if (x % 2) != 0:
    print("Try again!")
num = int(input("Enter a number: "))
check = int(input("Enter a second number: "))
if (num % check) == 0:
    print("Good Number!")
elif (num % check) != 0:
    print("Bad Number!")