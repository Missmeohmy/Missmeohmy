#This program will read through and parse a file with text and numbers.  It will extract all the numbers in the file nd compute the sum of the number.

import re
count = 0
with open("regex_sum_1804770.txt") as a:
    b = a.read()
c = re.findall('[0-9]+', b)
for d in range(0, len(c)):
    c[d] = int(c[d])
add = sum(c)
print(add)

