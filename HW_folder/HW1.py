def solution1(arr):
    answer = sum(arr) / len(arr)
    return answer

def solution2(num):
    if(num % 2 == 1):
        answer = 'Odd' 
    else: 
        answer = 'Even'
    return answer

def solution3(n):
    answer = 0
    for i in range(1,n + 1): 
        if(n % i == 0): answer +=i
    return answer

def solution4(n):
    answer = 0

    while(n > 0):
        answer += (n % 10)
        n //=10

    return answer

def solution5(x, n):
    answer = []
    for i in range(n):
        answer.append(x + x * i)
    return answer

def solution6(s):
    P = 0
    Y = 0
    
    for i in s.upper():
        if (i == "Y"):
            Y += 1
        elif (i == "P"):
            P += 1
    
    if(P == Y):
        return True
    else:
        return False
    
def solution7(n):
    for i in range(1, n+1):
        if(n % i == 1):
            return i
        
