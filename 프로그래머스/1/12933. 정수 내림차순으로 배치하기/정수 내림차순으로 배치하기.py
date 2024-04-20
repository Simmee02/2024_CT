def solution(n):
    n_list = []
    n=str(n)
    for i in range(len(n)):
        n_list.append(int(n[i]))
    n_list.sort()
    n_list.reverse()
    
    return int(''.join(str(num) for num in n_list))