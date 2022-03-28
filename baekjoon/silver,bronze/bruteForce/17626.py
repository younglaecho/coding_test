n = int(input())

if int(n ** (1 / 2)) == n ** (1 / 2):
    print(1)
    exit()

for i in range(int(n ** (1 / 2)) + 1):
    if int((n - i**2) ** (1 / 2)) == (n - i**2) ** (1 / 2):
        print(2)
        exit()

for i in range(int(n ** (1 / 2)) + 1):
    for j in range(int(n ** (1 / 2)) + 1):
        if (n - i**2 - j**2) > 0:
            if int((n - i**2 - j**2) ** (1 / 2)) == (n - i**2 - j**2) ** (
                1 / 2
            ):
                print(3)
                exit()

print(4)

# n = int(input())
# cnt = 0
# List1 = set()
# while True:
#     cnt += 1
#     if cnt**2 <= n:
#         List1.add(cnt**2)
#     else:
#         break

# List2 = set()
# List3 = set()

# if n in List1:
#     print(1)
# else:
#     for i in List1:
#         for j in List1:
#             List2.add(i + j)

#     if n in List2:
#         print(2)

#     else:
#         for i in List1:
#             for j in List2:
#                 List3.add(i + j)

#         if n in List3:
#             print(3)

#         else:
#             print(4)

# 4
