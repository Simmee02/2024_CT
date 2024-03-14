N,M= map(int,input().split())
list=[]

for i in range(N):
    list.append(i+1)

for i in range(M):
    I,J= map(int,input().split())
    list[I-1:J]=reversed(list[I-1:J])

print(' '.join(map(str,list)))


