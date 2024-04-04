nums=list(map(int,input().split()))
nums.sort()
a,b,c=nums
if a == b == c:
    print(a + b + c)
elif a+b <= c:
    print(2*a+2*b-1)
else:
    print(a + b + c)