def solution(s):
    temp = 0
    for i in range(len(s)):
        if s[i] == "(":
            temp += 1
        else:
            temp -= 1
        if temp < 0:
            return False
            break
    if temp == 0:
        return True
    else:
        return False
            
