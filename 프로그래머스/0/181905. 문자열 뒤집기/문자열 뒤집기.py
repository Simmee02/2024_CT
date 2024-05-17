def solution(my_string, s, e):
    answer = ''
    reverse = ''
    
    reverse = my_string[s:e+1]
    reverse = reverse[::-1]
    
    answer = my_string[:s] + reverse + my_string[e+1:]
    
    
    return answer