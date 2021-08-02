data = input()

medium = int(len(data)/2)
left = 0
right = 0
print(medium)
for number in data[0:medium]:
    left += int(number)
for number in data[medium:]:
    right += int(number)

if left == right:
    print('lucky')
else:
    print('ready')
