N,M = map(int,input().split())
S = set()
temp = 0

for i in range(N):
    word = input()
    S.add(word)

for i in range(M):
    word = input()
    if word in S:
        temp+=1

print(temp)
