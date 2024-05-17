import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)

def dfs(graph, node, visited):
    global order
    visited[node] = order
    order += 1
    for next_node in sorted(graph[node]):
        if visited[next_node] == 0:
            dfs(graph, next_node, visited)

# 입력
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

# 방문 순서 초기화
visited = [0] * (N + 1)
order = 1

# DFS 수행
dfs(graph, R, visited)

# 방문 순서 출력
for i in range(1, N + 1):
    print(visited[i])
