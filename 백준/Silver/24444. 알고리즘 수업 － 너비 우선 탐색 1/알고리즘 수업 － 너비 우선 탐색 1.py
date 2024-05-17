from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    queue = deque([start])  # deque를 사용하여 큐 초기화
    visited[start] = 1      # 시작 정점을 방문 처리
    count = 2               # 방문 순서 카운트

    while queue:
        v = queue.popleft()  # 큐의 앞에서 정점 꺼내기

        for i in sorted(graph[v]):  # 인접 정점을 오름차순으로 방문
            if not visited[i]:      # 인접 정점이 방문되지 않았다면
                queue.append(i)     # 큐에 추가
                visited[i] = count  # 방문 순서 기록
                count += 1

# 입력 처리
import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
M = int(data[1])
R = int(data[2])

graph = [[] for _ in range(N + 1)]
index = 3
for _ in range(M):
    a = int(data[index])
    b = int(data[index + 1])
    graph[a].append(b)
    graph[b].append(a)
    index += 2

# 방문 리스트 초기화
visited = [0] * (N + 1)

# BFS 수행
bfs(graph, R, visited)

# 방문 순서 출력
for i in visited[1:]:
    print(i)
