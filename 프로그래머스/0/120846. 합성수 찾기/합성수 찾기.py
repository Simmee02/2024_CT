def solution(n):
    answer = 0
    for i in range(n+1):
        count=0
        for j in range(1,int((i**0.5)+1)):
            if i%j == 0:
                count = count + 1
                if j != i // j:  
                    count += 1
        if count >= 3:
            answer += 1
                  
    return answer