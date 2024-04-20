def solution(seoul):
    i = 0
    while True:
        if seoul[i] == 'Kim':
            return "김서방은 "+str(i)+"에 있다"
        else:
            i = i+1
        
            