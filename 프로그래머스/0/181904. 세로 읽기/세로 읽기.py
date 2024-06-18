def solution(my_string, m, c):
    ans = ""
    my_string = list(my_string)
    res = []
    for i in range(len(my_string)//m):
        res.append(my_string[i*m+(c-1)])
    
    ans = ''.join(res)
        
    
    return ans