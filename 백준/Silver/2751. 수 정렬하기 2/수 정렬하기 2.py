import sys
N = int(sys.stdin.readline())
nums = []

for i in range(N):
    a = int(sys.stdin.readline())
    nums.append(a)

nums.sort()
for i in range(N):
    print(nums[i])