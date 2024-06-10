from collections import deque
n, m = map(int, input().split())

# 인접 리스트, 방문 리스트 생성
graph = []
visit = []

graph.append([0]*(m+2))
for _ in range(n):
    graph.append([0]+list(map(int, input().split()))+[0])
graph.append([0]*(m+2))

# BFS 큐 생성(deque 사용)
def bfs(x, y):
    Q = deque()
    Q.append((x, y, 1))
    count = 0
    
    dx = [-1, 0, 1, 0] # 북쪽부터 시계방향
    dy = [0, 1, 0, -1]
    
    # 방문 리스트 초기화
    for _ in range(n+2):
        visit.append([False] * (m+2))

    # 현재 노드가 1이고, 아직 방문하지 않았을 시 방문 처리
    if graph[x][y] == 1 and visit[x][y] == False:
        visit[x][y] = True

    while Q:
        (x, y, count) = Q.popleft() # 방문 노드 처리(큐로 처리하기 위해 왼쪽에서부터 꺼냄)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (1 <= nx <= n) and (1 <= ny <= m):
                if graph[nx][ny] == 1 and not visit[nx][ny]:
                    if nx == n and ny == m:
                        return count + 1
                    visit[nx][ny] == True
                    Q.append((nx, ny, count + 1))

print(bfs(1,1))