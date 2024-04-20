def solution(x):
    sum=0
    x_str = str(x)
    for i in range(len(str(x))):
        sum = int(x_str[i]) + sum
    if x % sum == 0:
        return True
    else:
        return False
        