N,M,V = map(int,input().split())

#1.그래프 초기화,간선 정보 입력
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


#dfs정의
#graph = 인접 리스트로 표현된 그래프
#start = 탐색을 시작할 정점
#visited = 각 정점의 방문 여부를 기록하는 리스트
#dfs_result = 방문 순서를 기록하는 리스트
def dfs (graph, start, visited):
    visited[start] = True
    dfs_result.append(start)
    for next_node in sorted(graph[start]):
        if not visited[next_node]:
            dfs(graph,next_node,visited)

def bfs(graph,start):
    queue = [start]
    visited = [False] * (len(graph))
    visited[start] = True
    bfs_result = []

    while queue:
        node = queue.pop(0)
        bfs_result.append(node)
        for next_node in sorted(graph[node]):
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

    return bfs_result



dfs_result = []
visited = [False] * (N + 1)
dfs(graph, V, visited)

# BFS 실행
bfs_result = bfs(graph, V)

# 결과 출력
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
