a, b = map(int, input().split())

prime_list = [True] *(b+1)
prime_list[1] = False

for i in range(2, int(b**0.5)+1):
    if prime_list[i]:
        for j in range(2, b):
            if i*j>b :
                break
            prime_list[i*j] = False

prime_count_list = [0] * (b + 1)

for i in range(1, b+1):
    if prime_list[i]:
        prime_count_list[i] = 1
        
for i in range(2, b+1):
    for j in range(2, b+1):
        if i * j > b :
            break
        if prime_list[j]:
            prime_count_list[i*j] = prime_count_list[i] + 1

result = 0
for i in range(a, b+1):
    if prime_list[prime_count_list[i]]:
        result += 1

print(result)



# def checkUnderPrime(n):
#     cnt = 0
#     k = 2
#     while True:
#         for i in range(k, n+1):
#             if n%i==0:
#                 cnt +=1
#                 n = int(n/i)
#                 k = i
#                 break
#         if n == 1:
#             break
#     if checkPrime(cnt):
#         return True
#     else:
#         return False
    
    
# def checkPrime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n**(1/2))+1):
#         if n%i==0:
#             return False
#     return True

# result = 0
# for i in range(a, b+1):
#     if checkUnderPrime(i):
#         result+=1

# print(result)