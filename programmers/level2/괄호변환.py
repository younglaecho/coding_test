def is_bal(p):
    bal = 0

    for bracket in p:
        if bracket == '(':
            bal += 1
        else:
            bal -= 1
    return not(bool(bal))

def is_right(p):
    bal = 0
    
    if is_bal(p) == False:
        return False
    for bracket in p:
        if bracket == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0: return False
    return True
       
def solution(p):
    answer = ''
    if is_right(p) == True:
        return p
    for i in range(2, len(p)+1,2):
        if is_bal(p[:i])==True:
            u, v = p[:i], p[i:]
            a = 1
            break
    if is_right(u) == True:
        return u + solution(v)
    else:
        result = '(' + solution(v) + ')'
        for i in u[1:-1]:
            if i == '(':
                result += ')'
            else:
                result += '('
        return result