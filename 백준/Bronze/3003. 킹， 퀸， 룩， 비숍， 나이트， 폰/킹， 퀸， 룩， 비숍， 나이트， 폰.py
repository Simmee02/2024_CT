chess_list=[1,1,2,2,2,8]

numbers = list(map(int,input().split()))

temp=[]
loss=0

for i in range(6):
    if chess_list[i] == numbers[i]:
       temp.append(0)
    else:
        loss= chess_list[i]-numbers[i]
        temp.append(loss)

print(' '.join(map(str,temp)))