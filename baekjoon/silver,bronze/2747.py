# def fibo(x):
#   if x == 0:
#     return 0
#   elif x == 1:
#     return 1
#   else:
#     return fibo(x-1) + fibo(x-2)

# print(fibo(int(input())))

n = int(input())

a, b = 0, 1

while n > 0:
  a, b = b, a+b
  n -= 1

print(a)

# n = int(input())

# arr = [0,1,1]*16

# for i in range(3,n+1):
#   arr[i] = arr[i-2]+arr[i-1]

# # print(arr)
# print(arr[n])