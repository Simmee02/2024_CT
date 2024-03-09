N= int(input())
list=[]

for i in range(N):
    s= input()
    list.append(s[0])
    list.append(s[-1])
    print(''.join(map(str,list)))
    list.remove(s[0])
    list.remove(s[-1])
