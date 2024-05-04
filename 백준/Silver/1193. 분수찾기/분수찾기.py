import sys
input = sys.stdin.read

X = int(input())

# 1. 대각선 찾기
n = 1
while (n * (n + 1)) // 2 < X:
    n += 1

# 2. 대각선의 어느 위치에 있는지 찾기
position = X - (n * (n - 1)) // 2

# 3. 분수 표현
if n % 2 == 0:  # 짝수 대각선
    numerator = position
    denominator = n - position + 1
else:  # 홀수 대각선
    numerator = n - position + 1
    denominator = position

print(f"{numerator}/{denominator}")
