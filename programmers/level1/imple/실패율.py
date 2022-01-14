def solution(N, stages):
    loseRates = []
    count = len(stages)
    for i in range(1, N+1):
        if count != 0:
            loseRate = stages.count(i)/count
            count-= stages.count(i)
            loseRates.append((loseRate,i))
        else:
            loseRates.append((0,i))
    loseRates.sort(key=lambda x:(-x[0]))
    answer = [i[1] for i in loseRates]
    return answer