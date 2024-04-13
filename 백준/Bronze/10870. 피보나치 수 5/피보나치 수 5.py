def fibonaccci(x):
    a = 0
    b = 1
    result = 0
    if x == 0:
        print(0)
    elif x == 1:
        print(1)
    else:
        for i in range(x - 1):
            result = a + b
            a = b
            b = result
        print(result)

fibonaccci(int(input()))
