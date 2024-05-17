import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.read
# 데이터 분할
data = input().split()
N = int(data[0])
M = int(data[1])
R = int(data[2])

#그래프 그리시 시간 준 버전
graph = [[] for _ in range(N + 1)]
index = 3
for _ in range(M):
    a = int(data[index])
    b = int(data[index + 1])
    graph[a].append(b)
    graph[b].append(a)
    index += 2

def dfs (graph,node,visited):
    global order
    visited[node] = order
    order +=1
    for next_node in sorted(graph[node],reverse=True):
        if visited[next_node] == 0:
            dfs(graph,next_node,visited)

visited = [0] * (N+1)
order = 1
dfs(graph,R,visited)

for i in range(1, N + 1):
    print(visited[i])
