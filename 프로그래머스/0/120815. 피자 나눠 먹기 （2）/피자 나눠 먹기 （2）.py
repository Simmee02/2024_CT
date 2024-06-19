def solution(n):
    answer = 0
    #최소공배수 구하는 문제
    nums = [2,3]
    num = 6
    temp = 1
    for i in range(2):
        if n%nums[i] == 0:
            temp = temp * nums[i]
            n = n//nums[i]
            num = num//nums[i]
    temp = num * temp * n 
    answer = temp//6      
    return answer