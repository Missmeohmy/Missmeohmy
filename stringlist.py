#This program will ask the user for a string and print out whether this string is a palindrome or not#
def convert(string):
    list1 = []
    list1[:0] = string
    return list1

x = input("Please type a sentence: ")
x = x.replace(" ", "")
print(convert(x))
if convert(x) == convert(reversed(x)):
    print("Congrats on your palindrome!")
else:
    print("Oh no! This one's not your pal-indrome")