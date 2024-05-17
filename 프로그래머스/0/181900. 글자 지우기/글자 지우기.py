def solution(my_string, indices):
    ans = ''
    
    my_string = list(my_string)
    for index in sorted(indices,reverse=True):
        del my_string[index]
    
    return ''.join(my_string)