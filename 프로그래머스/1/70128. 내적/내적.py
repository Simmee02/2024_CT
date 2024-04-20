def solution(a, b):
    ans = 0
    for i in range(len(a)):
        ans = ans + a[i]*b[i]
    return ans