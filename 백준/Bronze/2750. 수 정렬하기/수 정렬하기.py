N = int(input())
nums =[]
for i in range(N):
    a=int(input())
    nums.append(a)

nums.sort()
for i in range(len(nums)):
    print(nums[i])