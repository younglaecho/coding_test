size_x, size_y = list(map(int, input().split()))
x, y, direction = list(map(int, input().split()))

game_map = []
for _ in range(size_x):
    game_map.append(list(map(int, input().split())))

dir_move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
game_map[x][y] = -1


def show_map(map):
    for i in map:
        row = ''
        for j in i:
            row += str(j) + ' '
        print(row)


count = 1
turn_time = 0
while True:
    direction -= 1
    if direction == -1:
        direction = 3
    next_x = x + dir_move[direction][0]
    next_y = y + dir_move[direction][1]

    if game_map[next_x][next_y] == 0:
        game_map[next_x][next_y] = -1
        x = next_x
        y = next_y
        count += 1
        turn_time = 0
        show_map(game_map)
        print('----------------')

    else:
        turn_time += 1

    if turn_time == 4:
        next_x = x - dir_move[direction][0]
        next_y = y - dir_move[direction][1]

        if game_map[next_x][next_y] == 1:
            break
        else:
            x = next_x
            y = next_y
        turn_time = 0

print(count)
