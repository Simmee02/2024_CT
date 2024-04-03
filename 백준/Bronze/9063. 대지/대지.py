N = int(input())

x=[]
y=[]

large_x=-10000
large_y=-10000
small_x = 10000
small_y = 10000

for i in range(N):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

for i in range(N):
    if x[i]>=large_x:
        large_x = x[i]
    if x[i]<=small_x:
        small_x = x[i]
    if y[i]>=large_y:
        large_y = y[i]
    if y[i]<=small_y:
        small_y = y[i]

print((large_x-small_x)*(large_y-small_y))