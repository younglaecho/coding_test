def solution(arr, processes):
    # ["1","2","4","3","3","4","1","5"]	
    # ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
    # ["24","3415","4922","12492215","13"]
    from collections import deque

    result = []

    ing_process_time = 0

    time = 0
    processes.reverse()
    delay_r_process = deque()
    delay_w_process = deque()

    start_time1 = int(processes[-1].split()[1])
    status = 'empty'
    minus = 0

    while time<1101:
        time+=1
        # 시간이 흐름에 따라 진행중인process 들에 대한 갱신
        # ing_process = list(map(lambda x: int(x[2])-1, ing_process))
        ing_process_time-=1
        # 우리가 받아야 할 아이에 대한 정보
        if processes:
            ready_processes = processes[-1]
            process_param = ready_processes.split()
            # print(process_param)
            cur_status = process_param[0]
            start_time = int(process_param[1])
            during_time = int(process_param[2])
            start_idx = int(process_param[3])
            end_idx = int(process_param[4])

        # print(status)
        # print(cur_status)
        # 받을 시간이 되었을 때,
        if start_time==time:
            if processes:
                processes.pop()

            # 비어있다면,
            if status=='empty':
                if cur_status=='read':
                    ing_process_time = during_time
                    # ing_process.append()
                    status = 'r'
                    result.append("".join(arr[start_idx:end_idx+1]))
                    # print('---')
                else:
                    ing_process_time = during_time
                    # ing_process.append()
                    status = 'w'
                    for i in range(start_idx, end_idx+1):
                        arr[i] = process_param[5]
                        
            # 비어있지 않고, 쓰기모드라면
            elif status=='w':
                if cur_status =='write':
                    delay_w_process.append((during_time, start_idx, end_idx, process_param[5]))
                else:
                    delay_r_process.append((during_time, start_idx, end_idx))

            # 비어있지 않고, 읽기모드라면
            elif status=='r':
                if cur_status =='write':
                    delay_w_process.append((during_time, start_idx, end_idx, process_param[5]))
                else:
                    delay_r_process.append((during_time, start_idx, end_idx))

        
        # 모든 프로세스가 끝났다면
        if not ing_process_time:
            if delay_w_process:
                cur_process = delay_w_process.popleft()
                ing_process_time = cur_process[0]
                start_idx = cur_process[1]
                end_idx = cur_process[2]
                status = 'w'
                for i in range(start_idx, end_idx+1):
                    arr[i] = cur_process[3]
            elif delay_r_process:
                for _ in range(len(delay_r_process)):
                    cur_process = delay_r_process.popleft()
                    during_time= cur_process[0]
                    ing_process_time = max(during_time, ing_process_time)
                    start_idx = cur_process[1]
                    end_idx = cur_process[2]
                    result.append("".join(arr[start_idx:end_idx+1]))
                status = 'r'
            else:
                status='empty'
                minus+=1
                last_time = time
    result.append(str(last_time-minus-start_time1))
    return result


arr= ["1","2","4","3","3","4","1","5"]	
processes = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
solution(arr, processes)

# arr = ["1", "1", "1", "1", "1", "1", "1"]
# processes = ["write 1 12 1 5 8", "read 2 3 0 2", "read 5 5 1 2", "read 7 5 2 5", "write 13 4 0 1 3", "write 19 3 3 5 5", "read 30 4 0 6", "read 32 3 1 5"]
# solution(arr, processes)