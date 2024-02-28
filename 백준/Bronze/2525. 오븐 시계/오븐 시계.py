A,B = map(int,input().split())
C=int(input())


if C<60:
    if B+C < 60:
        B=B+C
    else:
        A= A+1
        B= (B+C)-60

else:
    A=round(C//60)+A
    
    if B+C%60 < 60:
        B=C%60+B
    else:
        A=A+1
        B=(B+C%60)-60

print(A%24,B)    
    