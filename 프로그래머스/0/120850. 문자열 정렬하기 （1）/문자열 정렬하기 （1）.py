def solution(my_string):
    answer = []
    digits = [str(i) for i in range(10)]  

    for char in my_string:
        if char in digits:
            temp = int(char)
            answer.append(temp)
    
    answer.sort()
    
    return answer
