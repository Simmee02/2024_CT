def numbers (x,y):
    if x<y:
        if y%x == 0:
            print("factor")
        else:
            print("neither")
    else:
        if x%y == 0:
            print("multiple")
        else:
            print("neither")


while True:
    a,b=map(int,input().split())
    if a+b ==0:
        break
    numbers(a, b)