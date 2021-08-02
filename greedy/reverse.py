from distutils.filelist import findall
import re
data = input()


p0 = re.compile('(0)+')
p1 = re.compile('(1)+')
a = p0.findall(data)
b = p1.findall(data)
print(min(len(a), len(b)))
