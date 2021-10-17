
def solution(record):
    answer = []
    dict = {}
    for states in record:
        stateList = states.split(' ')
        if stateList[0] == 'Enter' or stateList[0] =='Change':
            dict[stateList[1]]=stateList[2]
            
    for states in record:
        result = ''
        stateList = states.split(' ')
        result += dict[stateList[1]] +'님이 '
        if stateList[0] == 'Change':
            continue
        if stateList[0] == 'Enter':
            result += '들어왔습니다.'
        else :
            result += '나갔습니다.'
        answer.append(result)
    return answer