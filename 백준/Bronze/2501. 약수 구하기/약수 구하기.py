N,K = map(int,input().split())
numbers = []

for i in range(N+1):
    if N%(i+1) == 0:
        numbers.append(i+1)

if len(numbers) > K-1 :
    print(numbers[K - 1])
else:
    print("0")

