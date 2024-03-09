N,M= map(int,input().split())
list=[]
for i in range(N):
    list.append(i+1)

for j in range(M):
    a,b= map(int,input().split())
    X= list[a-1]
    Y= list[b-1]
    list[a - 1]= Y
    list[b - 1]= X

print(' '.join(map(str,list)))