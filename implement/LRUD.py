size = int(input())
move = input().split()

movement = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
position = [1, 1]
for i in range(len(move)):
    position[0] += movement[move[i]][0]
    position[1] += movement[move[i]][1]
    if position[0] == 0:
        position[0] = 1
    if position[0] == size+1:
        position[0] = size
    if position[1] == 0:
        position[1] = 1
    if position[1] == size+1:
        position[1] = size

print(position[0], position[1])
