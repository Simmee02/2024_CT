N = int(input())

for i in range(N):
    a,b = map(int,input().split())
    temp = 1
    for k in range(1,a+1):
        temp = temp * (b-k+1)// k
    print(temp)