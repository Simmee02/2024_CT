x,y,w,h = map(int,input().split())

distance = [x,y,w-x,h-y]
temp=1000

for i in range(4):
    if distance[i]<temp:
        temp = distance[i]

print(temp)