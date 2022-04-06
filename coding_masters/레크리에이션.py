n = int(input())

arr = list(map(int, input().split()))

start, end = map(int, input().split())

print(min(arr[start - 1 : end]))
