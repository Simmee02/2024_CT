A,B = map(int,input().split())

if B-45<0:
    B = B + 15
    if A == 0:
        A = 23
    else:
        A=A-1
else:
    B=B-45

print(A,B)
