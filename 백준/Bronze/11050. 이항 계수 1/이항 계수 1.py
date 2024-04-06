a,b = map(int,input().split())
result = 1
temp = 1
m = 1
for i in range(1,a+1):
    result = i*result
for j in range(1,b+1):
    temp = j*temp
for k in range(1,a-b+1):
    m =  k*m

print(result//(temp*m))