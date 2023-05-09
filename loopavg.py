#This program will add the show the average of the items within a loop
count = 0
sum = 0
print("Start", count)
for num in [1, 63, 6, 89, 22, 45, 96, 3, 6, 45, 77, 100, 352, 6251, 987, 663]:
    count = count + 1
    sum = sum + num
    print(count, sum, num)
print("End", count, sum, sum / count)