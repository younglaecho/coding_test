position = input()
alnum = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
x = alnum[position[0]]
y = int(position[1])

movements = [[2, 1], [1, 2], [-1, 2], [-2, 1],
             [-2, -1], [-1, -2], [1, -2], [2, -1]]

count = 0
for movement in movements:
    if 0 < (x + movement[0]) < 9 and 0 < (y + movement[1]) < 9:
        count += 1

print(count)
