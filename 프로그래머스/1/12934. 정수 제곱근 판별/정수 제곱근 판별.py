def solution(n):
    ans=0
    i=0
    while (i*i <= n):
        i += 1
        
    if (i-1)*(i-1) == n:
        ans = i*i
    else:
        ans = -1
    return ans
        