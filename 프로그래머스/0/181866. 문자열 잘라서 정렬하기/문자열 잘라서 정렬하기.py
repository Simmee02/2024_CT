def solution(myString):
    answer = []
    start = 0
    end = 0
    
    for i in range(len(myString)):
        if myString[i] == "x":
            end = i
            if myString[start:end] != "":
                answer.append(myString[start:end])
            start = end + 1
            
            
    if myString[len(myString)-1] != "x":
        answer.append(myString[start:len(myString)])
    
    answer = sorted(answer)
    
    return answer