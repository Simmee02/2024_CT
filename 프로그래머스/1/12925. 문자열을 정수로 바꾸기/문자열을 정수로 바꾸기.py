def solution(s):
    num = 0
    start_index = 1 if s[0] == '-' or s[0] == '+' else 0
    sign = -1 if s[0] == '-' else 1

    for i in range(start_index, len(s)):
        num = num * 10 + int(s[i])

    return sign * num