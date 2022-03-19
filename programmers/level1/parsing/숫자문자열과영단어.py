def solution(s):
    Dict = {'zero': '0', 'one': '1', 'two':'2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    answer = ''
    number = ''
    for Str in s:
        if Str.isdigit():
            answer+=Str
        elif Str.isalpha():
            number +=Str
            if number in Dict.keys():
                answer += Dict[number]
                number = ''
    return int(answer)