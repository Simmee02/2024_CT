N= int(input())
list=[]

for i in range(N):
    s= input()
    str= s[0] + s[-1]
    str.replace(" ","")
    print(str)