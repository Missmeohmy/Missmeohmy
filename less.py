a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x < 5:
        b = []
        b.append(x)
        print(b)
c = int(input("Enter a number: "))
for y in a:
    if y<c:
        print(y)