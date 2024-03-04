list=[]

for i in range (9):
    a=int(input())
    list.append(a)

max_num=max(list)
count_num=list.index(max_num)

print(max_num)
print(count_num+1)