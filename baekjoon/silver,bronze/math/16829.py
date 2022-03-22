n = int(input())

Str = input()

number = 0
answer = 0

for alpha in Str:
    result = (ord(alpha)-96)
    for _ in range(number):
        result*=31
        result%=1234567891
   
    number+=1
    answer+=result
print(answer%1234567891)