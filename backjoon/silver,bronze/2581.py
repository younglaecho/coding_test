start_num = int(input())
last_num = int(input())

result_list = []
for num in range(start_num, last_num+1):
    breaked = False
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                breaked = True
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if not breaked:
            result_list.append(num)  # error가 없으면 소수리스트에 추가
            
if len(result_list) > 0 :
    print(sum(result_list))
    print(min(result_list))
else:
    print(-1)