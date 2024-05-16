def solution(n):
    ans = 0
    R=[]
    
    if n <= 2:
        return n
        
    
    while True:
        R.append(n%3)
        n=n//3
        if n<= 2:
            R.append(n)
            break
            
    R.reverse()
    
    for i in range(len(R)):
        ans = ans + R[i]*(3**i)
          
    return ans