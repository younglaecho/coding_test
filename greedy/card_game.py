row_len, col_len = list(map(int, input().split()))

minimum = []
for i in range(row_len):
    row = list(map(int, input().split()))
    minimum.append(min(row))

print(max(minimum))
