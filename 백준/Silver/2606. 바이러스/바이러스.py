#그래프 초기회
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]


result = []
visited = [False]*(N+1)
#간선 정보 입력
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#dfs함수
def dfs (graph,start,visited):
    visited[start] = True #현재 정점 방문을 처리
    result.append(start) #방문할 정점을 리스트에 추가
    for next_node in sorted(graph[start]):
        if not visited[next_node]:
            dfs(graph,next_node,visited)

dfs(graph,1,visited)
print(len(result)-1) #1번컴 제외


