def solution(s):
    answer = ''
    nums=[]
    nums= list(map(int,s.split()))
    max=-10000
    min=10000
    for i in range(len(nums)):
        if nums[i]>max:
            max = nums[i]
        if nums[i]<min:
            min = nums[i]
    answer = str(min)+" "+str(max)
    return answer