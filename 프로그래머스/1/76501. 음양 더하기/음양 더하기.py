def solution(absolutes, signs):
    ans = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            ans = ans + absolutes[i]
        else:
            ans = ans - absolutes[i]
    return ans
            