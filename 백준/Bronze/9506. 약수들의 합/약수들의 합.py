
def numbers (x):
    list = []
    for i in range(x-1):
        if x%(i+1) == 0:
            list.append(i+1)
    sum=0
    for j in range(len(list)):
        sum=sum+list[j]

    if sum == x:
        for k in range(len(list)):
            result = " + ".join(str(num) for num in list)
        print(str(x)+" = "+result)
    else:
        print(str(x)+" is NOT perfect.")


while True:
    n= int(input())
    if n == -1:
        break
    numbers(n)