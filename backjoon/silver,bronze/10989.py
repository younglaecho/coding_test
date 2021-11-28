import sys

input = sys.stdin.readline
n = int(input())
arr = [0]*10001

for _ in range(n):
  a= int(input())
  arr[a]+=1


for i in range(len(arr)):
  for j in range(arr[i]):
    print(i)