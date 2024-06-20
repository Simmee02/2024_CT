def solution(n):
    answer = 0
    factorial = 1
    i = 1
    
    while factorial <= n:
        factorial *= i
        i += 1
        
    answer = i - 2
    return answer
