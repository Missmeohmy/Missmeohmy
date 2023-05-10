#This code will prompt the user for numbers until they type done to end the program, it will display what was the largest and smallest number. Any other input will display invalid message
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        val = int(num)
    except:
        print("Invalid input")
        continue
    #for x in num:
    if largest is None:
        largest = val
    if smallest is None:
        smallest = val
    if largest < val:
        largest = val
    if smallest > val:
        smallest = val
        

print("Maximum is", largest)
print("Minimum is", smallest)