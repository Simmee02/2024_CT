N,M= map(int,input().split())
list= []

for z in range(N):
    list.append(0)

for x in range(M):
    i,j,k = map(int,input().split())
    for y in range(i,j+1):
        list[y-1]=k

print(' '.join(map(str, list)))
