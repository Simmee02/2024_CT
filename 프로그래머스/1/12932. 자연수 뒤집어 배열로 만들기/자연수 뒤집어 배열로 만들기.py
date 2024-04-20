def solution(n):
    n = str(n)
    n_list = []
    for i in range(len(n)):
        n_list.append(int(n[len(n)-1-i]))
    return n_list
    