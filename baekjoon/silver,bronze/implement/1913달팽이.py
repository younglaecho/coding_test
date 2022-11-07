n = int(input())
target = int(input())

def show(mat):
    for arr in mat:
        arr = list(map(str, arr))
        print(" ".join(arr))

matrix = [[0 for _ in range(n)] for _ in range(n)]
matrix[n//2][n//2] = 1

result = [n//2, n//2]

a = 1
for i in range(3, n+1, 2):
    num = i**2
    matrix[n//2-a][n//2-a] = num

    if num == target:
        result = [n//2-a, n//2-a]
    num -= 1


    for j in range(1, i):
        matrix[n//2-a+j][n//2-a] = num 
        if num == target:
            result = [n//2-a+j, n//2-a]
        num -= 1 

    for j in range(1, i):
        matrix[n//2-a+(i-1)][n//2-a+j] = num
        if num == target:
            result = [n//2-a+(i-1), n//2-a+j]
        num -= 1

    for j in range(1, i):
        matrix[n//2-a+(i-1)-j][n//2-a+(i-1)] = num
        if num == target:
            result = [n//2-a+(i-1)-j, n//2-a+(i-1)]
        num -= 1

    for j in range(1, i-1):
        matrix[n//2-a][n//2-a+(i-1)-j] = num
        if num == target:
            result = [n//2-a, n//2-a+(i-1)-j]
        num -= 1 
    a+=1

show(matrix)
x, y = result
print(x+1, y+1)