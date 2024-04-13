n = int(input())
nums = list(map(int,input().split()))
nums.sort()

if n%2 != 0:
    if n == 1:
        print(nums[0]*nums[0])
    else:
        print(nums[n//2]*nums[n//2])
else:
    print(nums[(n//2)-1]*nums[(n//2)])