def solution(s):
    ans = []
    nums =[]
    for i in range(len(s)):
        nums.append(int(ord(s[i])))  
    nums.sort()
    nums.reverse()
    for i in range(len(s)):
        ans.append(chr(nums[i]))
        
    return ''.join(ans)