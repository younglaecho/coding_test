def solution(n):
    answer = ''
    while n>=1 :
        if n%3==0:
            number = '4'
        elif n%3==1:
            number = '1'
        else:
            number = '2'
        answer = number + answer
        if n%3==0:
            n = (n-3)//3  
        else:
            n = (n-n%3)//3
    
    return answer

