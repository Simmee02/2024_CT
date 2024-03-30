N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(N - 2):
    for k in range(i + 1, N - 1):
        for j in range(k + 1, N):
            temp = cards[i] + cards[k] + cards[j]
            if result < temp <= M:
                result = temp

print(result)
