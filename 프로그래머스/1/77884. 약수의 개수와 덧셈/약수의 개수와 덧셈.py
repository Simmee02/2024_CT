def solution(left, right):
    answer = 0
    nums = []
    for i in range(right-left+1):
        nums.append(left+i)
    for i in range(len(nums)):
        temp = 0
        for j in range(1,nums[i]+1):
            if nums[i]%j == 0:
                temp +=1
        if temp%2 == 0:
            answer = answer + nums[i]
        else:
            answer = answer - nums[i]               
    return answer