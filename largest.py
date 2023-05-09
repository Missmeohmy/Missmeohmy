#This code will find the largest value
largest_now= -1
print('Before', largest_now)
for num in [20, 100, 65, 3, 99, 550, 90, 9]:
    if num > largest_now:
        largest_now = num
    print(largest_now, num)
print('After', largest_now)