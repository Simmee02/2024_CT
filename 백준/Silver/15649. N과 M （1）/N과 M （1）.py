def backtrack(sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N + 1):
        if i not in sequence:
            sequence.append(i)
            backtrack(sequence)
            sequence.pop()

N, M = map(int, input().split())
backtrack([])
