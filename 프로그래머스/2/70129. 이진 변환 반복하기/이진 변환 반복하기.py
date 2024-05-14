def solution(s):
    ans = []
    total_zeros = 0 
    transformations = 0  
    temp = 0
    
    while s != "1":
        count_ones = s.count('1')
        total_zeros += len(s) - count_ones 
        s= format(count_ones,'b')
        temp +=1
    ans.append(temp)
    ans.append(total_zeros)
    
    return ans
        