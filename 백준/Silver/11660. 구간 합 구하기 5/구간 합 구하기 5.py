import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n과 m 입력 받기
A = [[0] * (n + 1) for _ in range(n + 1)]  # A 행렬 초기화
D = [[0] * (n + 1) for _ in range(n + 1)]  # D 누적 합 행렬 초기화

# A 행렬 입력 받기
for i in range(1, n + 1):
    row = [0] + list(map(int, input().split()))
    A[i] = row

# D 행렬 계산 (누적 합)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 쿼리 처리 및 결과 출력
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
