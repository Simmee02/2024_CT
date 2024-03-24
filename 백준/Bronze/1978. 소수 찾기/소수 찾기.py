N = int(input())
numbers = list(map(int,input().split()))
sum = 0

for i in range(N):
    temp= numbers[i]
    x = 0
    if temp > 1:
        for j in range(temp):
            if temp%(j+1) == 0:
                x+=1
        if x<3:
            sum+=1

print(sum)
