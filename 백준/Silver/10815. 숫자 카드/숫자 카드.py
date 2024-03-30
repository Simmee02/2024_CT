import sys

N = int(sys.stdin.readline())
nums = set(map(int,input().split()))
M = int(input())
input_list = list(map(int, sys.stdin.readline().split()))
result = []
for i in range(M):
    if input_list[i] in nums:
        result.append("1")
    else:
        result.append("0")

print(" ".join(result))