T= int(input())
change_list=[]

for i in range(T):
    R, S = input().split()
    R = int(R)
    P = ""
    for char in S:
        P=P + char*R
    print(P)