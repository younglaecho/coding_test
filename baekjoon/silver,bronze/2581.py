start_num = int(input())
last_num = int(input())

result_list = []
for num in range(start_num, last_num+1):
    breaked = False
    if num > 1 :
        for i in range(2, num): 
            if num % i == 0:
                breaked = True
                break  
        if not breaked:
            result_list.append(num)  
            
if len(result_list) > 0 :
    print(sum(result_list))
    print(min(result_list))
else:
    print(-1)