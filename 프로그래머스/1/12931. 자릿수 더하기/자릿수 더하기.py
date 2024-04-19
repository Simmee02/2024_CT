def solution(n):
    sum=0
    n = str(n)
    for i in range(len(n)):
        sum = sum + int(n[i])
    
    return sum