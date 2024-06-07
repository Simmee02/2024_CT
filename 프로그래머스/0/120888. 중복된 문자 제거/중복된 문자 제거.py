def solution(my_string):
    answer = []
    seen = set()
    for char in my_string:
        if char not in seen:
            answer.append(char)
            seen.add(char)
    return ''.join(answer)
