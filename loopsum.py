#This program will add the items within a loop
count = 0
print("Start", count)
for num in [1, 63, 6, 89, 22, 45, 96, 3, 6, 45, 77, 100, 352, 6251, 987, 663]:
    count = count + num
    print(count, num)
print("End", count)