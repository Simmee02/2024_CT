list=[]
for i in range(30):
    list.append(i+1)

for i in range(28):
    a= int(input())
    list.remove(a)

print(' '.join(map(str,list)))