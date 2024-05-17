def solution(intStrs, k, s, l):
    ans = []

    for i in range(len(intStrs)):
        temp = 0
        nums = 0
        strs = intStrs[i]
        part = strs[s:s+l]
        nums = int(part)
        
        if nums > k:
            ans.append(nums)
        
    return ans