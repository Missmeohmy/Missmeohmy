a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
d = 0
for c in a:
    if c % 2 == 0:
        b.append(c)
        d = d +1
print(b)