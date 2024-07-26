def solution(myString, pat):
    answer = 0
    
    for i in range (len(myString)-len(pat)+1):
        word = ""
        for j in range(len(pat)):
            word = word + myString[i+j]
        
        if word == pat : 
            answer = answer + 1

    return answer
