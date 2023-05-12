# 2026 바이러스
# https://www.acmicpc.net/problem/2606
n = int(input())
c = int(input())
graph = []
for _ in range(c):
  graph.append(list(map(int, input().split())))
stack =[]
visited = [False]*(n+1)
def dfs(graph, visited,v):
    # 시작 노드 스택에 담기   
    stack.append(v) 
    # 스택에 방문하지 않은 인접 정점들을 담은 후 하나씩 빼오면서 탐색
    while stack:
        now = stack.pop()
        if now not in visited: 
          visited[now] = True
          for i in graph :
            if now in i:
              i.remove(now)
              stack.extend(i)
dfs(graph, visited, 1)
a = visited.count(False)
print(n-(a))