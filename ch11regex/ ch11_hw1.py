import re
import pprint
count = 0
lst = list()
fhand = open('regex_sum_42.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('[0-9]+', line):
        num = re.findall('[0-9]+', line)
        for dig in num:
            lst.append(dig)
            count = count + int(dig)


pprint.pprint(lst)
print(len(lst))
print(count)
