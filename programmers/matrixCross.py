def solution(arr1, arr2):
    matrix = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for z in range(len(arr2[0])):
            value = 0
            for j in range(len(arr1[0])):
                value += arr1[i][j]*arr2[j][z]
            matrix[i][z] = value
    return matrix