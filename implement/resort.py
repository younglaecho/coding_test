from ast import Num, Str
from curses.ascii import isalpha


data = input()

str1 = ''
num = 0
for i in data:
    if isalpha(i):
        str1 += i
    else:
        num += int(i)

sorted_str = sorted(str1)
str1 = ''.join(sorted_str)
str1 += str(num)

print(str1)
