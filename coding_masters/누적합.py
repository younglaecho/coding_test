n = int(input())

arr = list(map(int, input().split()))
length = len(arr)
tmp = 1

while length - tmp > 0:
    tmp = tmp * 2

arr += [0] * (tmp - length)

result = [arr]

tmp_arr = list(arr)
while tmp > 1:

    new_arr = []

    for i in range(0, tmp, 2):
        new_arr.append(tmp_arr[i] + tmp_arr[i + 1])

    result.append(new_arr)
    tmp_arr = list(new_arr)
    tmp //= 2

result.reverse()
for a in result:
    print(" ".join(map(str, a)))
